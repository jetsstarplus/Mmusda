from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models
from django.utils import timezone


def Index(request):
    scripture = models.Scripture.objects.order_by('-pub_date')[:1]
    visitor_word = models.visitor_word.objects.order_by('-pub_date')[:1]
    other_bussinesses = models.OtherBussiness.objects.order_by('-pub_date')[:3]
    event = models.Event.objects.order_by('-pub_date')[:6]
    eventOutline = models.Event.objects.order_by('-pub_date')[:1]
    annIndex = models.Announcement.objects.order_by('-announcement_due_date')[:8]
    
    context = { 
        'scripture': scripture,
         'visitor_word': visitor_word, 
         'other_bussinesses': other_bussinesses, 
         'event': event,
         'eventOutline': eventOutline,
        'annIndex':annIndex
     }
   
    return render(request, 'sda/index.html', context)
   
  
def Event(request, event_id):    
    item = get_object_or_404(models.Event, pk = event_id)
    otheritem = models.Event.objects.exclude(pk = event_id).order_by('-pub_date')[:4]
    details = models.EventsDetail.objects.filter(event = event_id).all()
    context = {
        'item':item,
        'otheritem':otheritem,
        'details':details
    }
    return render(request, 'sda/item.html', context)


def services(request):
    morning = models.services.objects.order_by('-day')
    morn = models.services.objects.order_by('-day')
    sabbath = models.services.objects.filter(day = "Saturday")
    context = {
        'morning':morning,
        'sabbath':sabbath,
        'morn':morn
    }
    return render(request, 'sda/services.html', context)

def dept_inside_activities(request):
    dept = models.Department.objects.filter(department_category = 'Internal Activities')
    leaders = models.Leaders_Department.objects.order_by('id')[:2]
    ann = models.Announcement.objects.order_by('-publication_date')[:10]
    event = models.Event.objects.order_by('-pub_date')[:10]
    context = {
        'dept':dept, 
        'leaders':leaders,
        'ann':ann,
        'event':event
    }
    return render(request, 'sda/dept_inside_activities.html', context)

def dept_members_welfare(request):
    dept = models.Department.objects.filter(department_category = 'Members Welfare')
    leaders = models.Leaders_Department.objects.order_by('id')[:2]
    ann = models.Announcement.objects.order_by('-publication_date')[:10]
    event = models.Event.objects.order_by('-pub_date')[:10]
    context = {
        'dept':dept, 
        'leaders':leaders,
        'ann':ann,
        'event':event
    }
    return render(request, 'sda/dept_members_welfare.html', context)

def dept_church_affairs(request):
    dept = models.Department.objects.filter(department_category = 'Church Affairs')
    leaders = models.Leaders_Department.objects.order_by('id')[:2]
    ann = models.Announcement.objects.order_by('-publication_date')[:10]
    event = models.Event.objects.order_by('-pub_date')[:10]
    context = {
        'dept':dept, 
        'leaders':leaders,
        'ann':ann,
        'event':event
    }
    return render(request, 'sda/dept_church_affairs.html', context)

def dept_ministries_outreach(request):
    dept = models.Department.objects.filter(department_category = 'Ministry & Outreach')
    leaders = models.Leaders_Department.objects.order_by('id')[:2]
    ann = models.Announcement.objects.order_by('-publication_date')[:10]
    event = models.Event.objects.order_by('-pub_date')[:10]
    context = {
        'dept':dept, 
        'leaders':leaders,
        'ann':ann,
        'event':event
    }
    return render(request, 'sda/dept_ministries_outreach.html', context)

def announcements(request):
    ann = models.Announcement.objects.filter(announcement_classification__startswith = 'Announcement')[:4]
    ann2 = models.Announcement.objects.filter(announcement_classification__startswith = 'Announcement')[:1]
    sub = models.Announcement.objects.filter(announcement_classification__startswith = 'Sub')[:5]

    context = {
        'ann': ann,
        'sub':sub,
        'ann2':ann2,
       
    }
    return render(request, 'sda/announcements.html', context)

def search(request):

    if request.method == "GET":
        form = request.GET.get('search')
        if form.is_valid():
            ann = models.Announcement.objects.filter(announcement_classification__startswith = 'Announcement')[:4]
            ann2 = models.Announcement.objects.filter(announcement_classification__startswith = 'Announcement')[:1]
            sub = models.Announcement.objects.filter(announcement_title__icontains = form)[:5]

            context = {
                'ann': ann,
                'sub':sub,
                'ann2':ann2,
            }
    return render(request, 'sda/search.html', context)


def sermons(request):
    itemother = models.Sermons.objects.order_by('publication_date')[:4]
    sermon = models.Sermons.objects.order_by('-publication_date')[:4]
    event = models.Event.objects.order_by('pub_date')[:5]
    context = {
        'sermon':sermon,
        'itemother':itemother,
        'event':event
    }
    return render(request, 'sda/sermons.html', context)

#this method explains in detail about the sermon to be discussed
def sermonDetail(request, sermon_id):
    item = get_object_or_404(models.Sermons, pk = sermon_id)
    other = models.Sermons.objects.exclude(pk = sermon_id).order_by('-publication_date')[:4]
    itemother = models.Sermons.objects.order_by('publication_date')[:4]
    event = models.Event.objects.order_by('pub_date')[:10]
    context = {
        'item':item,
        'other':other,
        'itemother':itemother, 
        'event':event
    }
    return render(request, 'sda/preaching-post.html', context)

#this represents the timeline page
def timeline(request):  
    timeline = models.Timeline.objects.filter(is_sabbath = True)
    timelines = models.Timeline.objects.filter(is_sabbath = False)
    event = models.Event.objects.order_by('pub_date')[:5]
    context = {
        'timeline':timeline, 
        'timelines':timelines, 
        'event':event
    }  
    return render(request, 'sda/timeline.html', context)

#it renders the about Page to the site
def about(request):
    about = models.About.objects.order_by('-pub_date')[:2]
    leader = models.Church_Member.objects.filter(is_leader = True)[:8]
    family = models.Family.objects.exclude(family_name = 'All')
    famLeader = models.Leaders_Family.objects.all()
    context = {
         'about': about,
         'leader':leader, 
         'family':family, 
         'famLeader':famLeader
    }
   
    return render(request, 'sda/about.html', context)

#This renders the Contact page to the site
def contact(request):
    # if request.method == 'POST'    
    contact = models.contact.objects.order_by('-pub_date')[:1]
    context = {
        'contact':contact
    }
    return render(request, 'sda/contact.html', context)


#This renders the faq to the actual MMU Website
class FAQView(generic.ListView):
    template_name = "sda/faq.html"
    context_object_name = 'faq'

    """Returning the  last faq"""
    def get_queryset(self):
        return models.faq.objects.order_by('-pub_date')[:10]
    
# Create your views here.
