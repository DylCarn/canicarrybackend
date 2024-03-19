from django.urls import include, path
from . import views
urlpatterns = [
    path("last_disclaimer/", views.ReturnLastDisclaimer.as_view()),
    path("sign_disclaimer/", views.SignDisclaimer.as_view()),
]