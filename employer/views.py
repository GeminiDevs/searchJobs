from django.shortcuts import render
from .models import Detail


# Create your views here.

def index(request):
    detail = Detail.objects.all()
    return render(request, 'index.html', {'detail': detail})


def employer(request):
    detail = Detail.objects.all()
    return render(request, 'employer.html', {'detail': detail})
