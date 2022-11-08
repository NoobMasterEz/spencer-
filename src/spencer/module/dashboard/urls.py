from django.views.generic.base import TemplateView
from django.urls import path, include

from .authentication.views import LoginViewSet


urls_dashboard = [
    path("dashboard/", TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
    path('dashboard/login/', LoginViewSet.as_view(), name="login"),
    path("dashboard/", include("django.contrib.auth.urls")),
]
