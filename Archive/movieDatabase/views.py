from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

def index(request):
    return render(request, "pages/index.html")

def movies(request):
    movie_list = Movie.objects.order_by("-movie_pub_date")
    return render(request, "pages/movies.html", {"movie_list": movie_list})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "pages/detail.html", {"movie": movie})

def loginPage(request):
    return render(request, "pages/login.html")

def registerPage(request):
    return render(request, "pages/register.html")

def about(request):
    return render(request, "pages/about.html")

def register(request):
    username = request.POST.get('username', False)
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)

    try:
        userExists = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, "pages/login.html")

    return render(request, "pages/register.html", {"error": "User already exists"})

def vote(movie_id, votes):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.votes += votes
    movie.save()

@login_required
def voteUp(request, movie_id):
    vote(movie_id, 1)
    return HttpResponseRedirect(reverse("detail", args=(movie_id,)))

@login_required
def voteDown(request, movie_id):
    vote(movie_id, -1)
    return HttpResponseRedirect(reverse("detail", args=(movie_id,)))

def login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pages/login.html", {"error": "Invalid username or password"})

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("index"))