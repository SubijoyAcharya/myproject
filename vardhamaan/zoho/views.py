from django.http import HttpResponse
from django.shortcuts import render
from .models import zoho


def index(request):
    products= zoho.objects.all()
    return render(request, 'index.html', {'products': products})


