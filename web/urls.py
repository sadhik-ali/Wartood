from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("updates/", views.blog, name="blog"),
    path("updatedetails/<int:id>/", views.blogdetails, name="blogdetails"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.project, name="project"),
    path("services/", views.service, name="service"),
    path("stone/", views.stone, name="stone"),
    path("servicedetails/<int:id>/", views.servicedetails, name="servicedetails"),
]
