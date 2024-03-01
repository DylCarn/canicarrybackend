from django.urls import include, path
from . import views
urlpatterns = [
    path("login/", views.LogIn.as_view()),
    path("logout", views.LogOut.as_view())
]