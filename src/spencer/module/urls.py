from django.urls import path, include
from django.views.generic.base import TemplateView

from .camera.views import video_feed, index
from .dashboard.authentication.views import LoginViewSet

urls_module = [
    path("dashboard/", include("django.contrib.auth.urls")),
    path("dashboard/", TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
    path('dashboard/login/', LoginViewSet.as_view(), name="login"),

    path('module/camera/', index, name='index'),
    path('module/camera/debug/', video_feed, name='video_feed'),
]
