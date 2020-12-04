from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # for the home page
    path("", views.project_index, name="project_index"),
    # for the projects detail page
    path("<int:project_id>/", views.project_details, name="project_details"),

]
