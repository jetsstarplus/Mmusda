from django.urls import path

from . import views


app_name = 'sda'
urlpatterns =[
    path('', views.Index, name = 'index'),
    path('services/', views.services, name = 'services'),
    path('dept_inside_activities/', views.dept_inside_activities, name = 'dept_inside_activities'),
    path('dept_members_welfare/', views.dept_members_welfare, name= 'dept_members_welfare'),
    path('dept_church_affairsView/', views.dept_church_affairs, name = 'dept_church_affairs'),
    path('dept_ministries_outreachView/', views.dept_ministries_outreach, name = 'dept_ministries_outreach'),
    path('announcements/', views.announcements, name = 'announcements'),
    path('about/', views.about, name = 'about'),
    path('sermons/', views.sermons, name = 'sermons'),
    path('timeline/', views.timeline, name = 'timeline'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('contact/', views.contact, name = 'contact'),
    path('item/<int:event_id>/', views.Event, name = 'item'),
    path('faq/', views.FAQView.as_view(), name = 'FAQ'),
    path('sermon/<int:sermon_id>/', views.sermonDetail, name = 'sermon'),

]