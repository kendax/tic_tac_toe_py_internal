from django.urls import path
from .views import HomePageView
from . import views

# Handle routing for this specific app (tic_tac_toe)
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("postinput/", views.gameSave, name="postform"),
    path("resultsValidation/", views.resultsValidation, name="validate"),
    path("restart/", views.restart, name="restart"),
]