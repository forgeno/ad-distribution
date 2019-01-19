from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Ad
# Create your views here.

class IndexView(generic.ListView):
    template_name = "adIndex/index.html"

    def get_queryset(self):
        return Ad.objects.all()