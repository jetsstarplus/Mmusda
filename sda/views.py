from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
from django.utils import timezone


def Index(request):
    scripture = models.Scripture.objects.order_by('-pub_date')[:1]
    visitor_word = models.visitor_word.objects.order_by('-pub_date')[:1]
    other_bussinesses = models.OtherBussiness.objects.order_by('-pub_date')[:3]
    event = models.Event.objects.order_by('-pub_date')[:6]
    
    context = { 
        'scripture': scripture,
         'visitor_word': visitor_word, 
         'other_bussinesses': other_bussinesses, 
         'event': event
     }
   
    return render(request, 'sda/index.html', context)
   
    


def Event(request):
    return render(request,'sda/item.html')


def services(request):
    return render(request, 'sda/services.html')

def dept_inside_activities(request):
    return render(request, 'sda/dept_inside_activities.html')

def dept_members_welfare(request):
    return render(request, 'sda/dept_members_welfare.html')

def dept_church_affairs(request):
    return render(request, 'sda/dept_church_affairs.html')

def dept_ministries_outreach(request):
    return render(request, 'sda/dept_ministries_outreach.html')

def announcements(request):
    return render(request, 'sda/announcements.html')


def sermons(request):
    return render(request, 'sda/sermons.html')

def timeline(request):
    return render(request, 'sda/timeline.html')

def about(request):
    about = models.About.objects.order_by('-pub_date')[:2]
   
    context = { 'about': about, }
   
    return render(request, 'sda/about.html', context)

def contact(request):
    return render(request, 'sda/contact.html')

class FAQView(generic.ListView):
    template_name = "sda/faq.html"
    context_object_name = 'faq'
    """Returning the  last faq"""
    def get_queryset(self):
        return models.faq.objects.order_by('-pub_date')[:10]
    
# Create your views here.
