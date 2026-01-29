from django.urls import path, re_path

from . import views

urlpatterns = [
    path("jobs/", views.jobpage_view, name="jobpage"),
    path("jobs/create", views.job_create, name="job_create"),
    path('jobs/toggle/<int:id>/', views.job_toggle, name="job_toggle"),
]