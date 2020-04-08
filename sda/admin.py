from django.contrib import admin
from . import models

#*****************Inlines**********************#
#this is a link between departments, family and leaders
class DptInline(admin.TabularInline):
    model = models.Leaders_Department
    extra = 0

class FamInline(admin.TabularInline):
    model = models.Leaders_Family
    extra = 0

#This is a link to the events
class detailInline(admin.TabularInline):
    model = models.EventsDetail
    extra = 0



#********************The actual tables in the admin Panel*****************************#

#The departments admin presentation
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_role')
    search_fields = ['department_name']
    list_filter = ['department_name']
    fieldsets = [
        ("Create A New Department", {'fields': ['department_name']}), 
        (None , {'fields': ['department_role']}), 
        (None, {'fields' : ['department_inspiration']}),
        (None, {'fields' : ['department_category']})

    ]
admin.site.register(models.Department, DepartmentsAdmin)


# #Church Leaders Admin Presentation
class ChurchLeadersAdmin(admin.ModelAdmin):

    list_display = ('full_name','contact')
    search_fields = ['first_name']
    fieldsets = [
        ('User', {'fields': ['user']}), 
        ('Phone Number', {'fields':['contact']}), 
        ('Year Of Admission', {'fields' : ['Adm_Year']})
    ]

    inlines = [DptInline, FamInline]

admin.site.register(models.Church_Member, ChurchLeadersAdmin)

#Family Representation

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'inspiration')
    search_fields = ['family_name']
    fieldsets = [
        ('Family Name', {'fields': ['family_name']}), 
        ('Family Inspiration', {'fields': ['inspiration']}), 
             
    ]

admin.site.register(models.Family, FamilyAdmin)

 

# This is the admin interface for the theme scripture and setting it to be visible
class Scripture(admin.ModelAdmin):
    date_heirarchy = ['pub_date']
    fieldsets = [
        ('Scripture Theme', {'fields': ['scripture_title']}),
        ('Scripture', {'fields' : ['scripture_content']}),
        ('Attached Verses', {'classes' : ['extrapretty'],'fields' : ['attached_verses']}),
        ('Date Published', {'classes': ['extrapretty'], 'fields' : ['pub_date']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['user_id']})
    ]

    list_filter = ['pub_date', 'scripture_title']
    search_fields = ['scripture_title']
    list_display = ('scripture_title',  'attached_verses' , 'user_id', 'status', 'was_published_recently')
    actions = ['make_inactive', 'make_active']

    # This action is used to show change the state of the
    #  scripture content and so as to make it more
    #  accessible and also readable

    def make_inactive(self, request, queryset):
        rowsupdated = queryset.update(status = "Inactive")
        if(rowsupdated == 1):
            message_bit = "1 Scripture Was"
        else:
            message_bit = "%s Scriptures Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked Inactive" %message_bit)

    make_inactive.short_description = "Mark the Selected Scripture as Inactive"

    def make_active(self, request, queryset):
        rowsupdated = queryset.update(status = "Active")
        if(rowsupdated == 1):
            message_bit = "1 Scripture Was"
        else:
            message_bit = "%s Scriptures Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked Active" %message_bit)
        
    make_active.short_description = "Mark the Selected Scriptures as Active"

admin.site.register(models.Scripture, Scripture)



# The class that handles all the event schedules alongside with their respective updates
class Event(admin.ModelAdmin):
    fieldsets = [
        ("Event Name", {'fields': ['event_name']}), 
        ("Description", {'fields': ['description']}),
        ("Image Link", {'fields': ['image_link']}),
        ("Due Date", {'fields': ['due_date']}),
        ("Family Responsible", {'fields': ['family_id']})
        
         ]


    #this returns the the title family responsible and the name in uppercase
    def family_name(self, obj):
        return ("%s" % (obj.family_id)).upper()


    family_name.short_description='Family Responsible'

    list_filter = ['pub_date', 'due_date', 'event_name']
    search_fields = ['event_name']
    list_display = ('event_name', 'due_date', 'is_date_due', 'family_name', 'was_published_recently')
    inlines = [detailInline]
    
admin.site.register(models.Event, Event)


#The frequently Asked Questions and their answers as made in the Admin Panel
class faq(admin.ModelAdmin):
    fieldsets = [
        ("Question", {'fields': ['question']}),
        ("Answer", {'fields': ['answer']}),
    ]

    list_filter = ['question']
    search_fields = ['question']
    list_display = ['question', 'was_published_recently']

admin.site.register(models.faq, faq)


# This is the class that describes the visitors word
class Visitor(admin.ModelAdmin):
    date_heirarchy = ['pub_date']
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Actual Salutation', {'fields' : ['content']}),
        ('Date Published', {'fields' : ['pub_date']}),
        (None, {'fields': ['user_id']})
    ]

    def created_by(self, obj):
        return ("%s " % (obj.user_id))
    
    created_by.short_description = "Written By"

    list_filter = ['pub_date', 'title']
    search_fields = ['title']
    list_display = ('title',  'created_by', 'was_published_recently')
  

admin.site.register(models.visitor_word, Visitor)


#Announcements Table
class announcement(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['announcement_title']}),
        ('Description', {'fields': ['announcement_description']}),
        ('Due Date', {'fields': ['announcement_due_date']}),
        (None, {'fields': ['publication_date']}),
        ('Posted By', {'fields': ['user_id']}),
        ('Advanced Options', {'fields': ['announcement_classification']}), 
        ('Advanced Options', {'fields': ['announcement_specification']})
    ]
    def created_by(self, obj):
        return ("%s " % (obj.user_id))

    created_by.short_description = "Posted By"

    list_filter = ['announcement_due_date', 'announcement_classification', 'publication_date']
    search_fields = ['announcement_due_date', 'announcement_title']
    list_display = ['announcement_title', 'is_date_due', 'created_by', 'was_published_recently', 'announcement_classification']

admin.site.register(models.Announcement, announcement)



# This is the class that describes the About Page
class About(admin.ModelAdmin):
    date_heirarchy = ['pub_date']
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Actual Salutation', {'fields' : ['content']}),
        ('Date Published', {'fields' : ['pub_date']}),
        (None, {'fields': ['user_id']})
    ]

    def created_by(self, obj):
        return ("%s " % (obj.user_id))
    
    created_by.short_description = "Written By"

    list_filter = ['pub_date', 'title']
    search_fields = ['title']
    list_display = ('title',  'created_by', 'was_published_recently')
  

admin.site.register(models.About, About)


# This is the class that describes the What appeas in the home page as the
# Other businesses and manipulation page in in the admin site Page
class OtherBussiness(admin.ModelAdmin):
    date_heirarchy = ['pub_date']
    fieldsets = [
        ('Title', {'fields': ['other_title']}),
        ('Description', {'fields' : ['other_description']}),
        ('Date Published', {'fields' : ['pub_date']}),
        (None, {'fields': ['user_id']})
    ]

    def created_by(self, obj):
        return ("%s " % (obj.user_id))
    
    created_by.short_description = "Written By"

    list_filter = ['pub_date', 'other_title']
    search_fields = ['other_title']
    list_display = ('other_title',  'created_by', 'was_published_recently')
  

admin.site.register(models.OtherBussiness, OtherBussiness)
# Register your models here.
