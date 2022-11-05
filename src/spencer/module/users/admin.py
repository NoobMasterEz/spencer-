from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm, User
# Register your models here.


@admin.register(User)
class CameraAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
