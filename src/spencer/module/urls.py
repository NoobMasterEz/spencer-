from django.urls import path

from .camera.views import video_feed, index
from .dashboard.urls import urls_dashboard

urls_module = [
    path('module/camera/', index, name='index'),
    path('module/camera/debug/', video_feed, name='video_feed'),
] + urls_dashboard
