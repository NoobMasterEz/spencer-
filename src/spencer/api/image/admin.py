from django.contrib import admin

from .models import ImageTransaction, Centroids, Camera


@admin.register(ImageTransaction)
class ImageTransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Centroids)
class CentroidsAdmin(admin.ModelAdmin):
    pass


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    pass
