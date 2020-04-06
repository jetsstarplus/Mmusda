from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/login/')
def home(request):
    return render(request, 'Mission/index.html')


def index(request):
    return render(request, 'sda/index.html')

def success(request):
    return render(request, 'Final/success.html')

def calendar(request):
    return render(request, 'Final/calendar.html')
# Create your views here.