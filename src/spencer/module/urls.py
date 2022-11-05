from django.urls import path, include
from django.views.generic.base import TemplateView

from .camera.views import video_feed, index
from .users.views import SignUpView

urls_module = [
    path("dashboard/", TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
    path("dashboard/", include("django.contrib.auth.urls")),
    path("dashboard/signup/", SignUpView.as_view(), name="signup"),

    path('module/camera/', index, name='index'),
    path('module/camera/debug/', video_feed, name='video_feed'),
]