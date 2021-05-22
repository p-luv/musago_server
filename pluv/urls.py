from django.urls import path, include

from . import views
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path("signup/", views.SignupView.as_view()),
    path("signup", views.SignupView.as_view()),
    path("point/", views.PointView.as_view()),
    path("login/", views.LoginView.as_view()),
]