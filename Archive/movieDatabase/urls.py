from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movies, name="movies"),
    path("movies/<int:movie_id>/", views.detail, name="detail"),
    path("movies/<int:movie_id>/voteUp/", views.voteUp, name="voteUp"),
    path("movies/<int:movie_id>/voteDown/", views.voteDown, name="voteDown"),
    path("login/", views.loginPage, name="loginPage"),
    path("login/submit", views.login, name="login"),
    path("register/", views.registerPage, name="registerPage"),
    path("register/submit", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
]
