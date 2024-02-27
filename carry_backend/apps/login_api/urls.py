from django.urls import include, path
from . import views
urlpatterns = [
    path("test/", views.UserViewSet.as_view()),
]