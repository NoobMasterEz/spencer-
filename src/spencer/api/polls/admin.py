from django.contrib import admin
from django import forms

from .models import polls

# Register your models here.


class PersonForm(forms.ModelForm):

    class Meta:
        model = polls
        exclude = ['name']


@admin.register(polls)
class Polls(admin.ModelAdmin):
    exclude = ['age']
    form = PersonForm
