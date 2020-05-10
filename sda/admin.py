from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

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
    list_display = ('department_name', 'department_role', 'department_category')
    search_fields = ['department_name']
    list_filter = ['department_name']
    fieldsets = [
        ("Create A New Department", {'fields': ['department_name']}), 
        (None , {'fields': ['department_role']}), 
        (None, {'fields' : ['department_inspiration']}),
        (None, {'fields' : ['department_category']})

    ]
admin.site.register(models.Department, DepartmentsAdmin)

#This is To create the Category and The leaders
class DepartmentCategory(admin.ModelAdmin):
    list_display = ('category_name','category_leader')
    search_fields= ['category_name']
    list_filter = ['publication_date']
    fieldsets = [
        ('Category Name', {'fields': ['category_name']}),
        (None, {'fields': ['Category_role']}),
        (None, {'fields': ['category_leader']}), 
        (None, {'fields': ['Word_From_The_Leader']})
    ]
    

admin.site.register(models.Department_Category, DepartmentCategory)

# #Church Leaders Admin Presentation
class ChurchLeadersAdmin(admin.ModelAdmin):

    list_display = ('profile','full_name','contact',  'is_leader')
    list_display_links = ['full_name']
    search_fields = ['user']
    fieldsets = [
        ('User', {'fields': ['user']}), 
        ('Phone Number', {'fields':['contact']}), 
        ('Year Of Admission', {'fields' : ['Adm_Year']}),
        (None, {'fields': ['is_leader']}), 
        (None, {'fields': ['profile_picture']})
    ]
    autocomplete_fields = ['user']
    inlines = [DptInline, FamInline]

     
    def profile(self, obj):
        return mark_safe('<img src = "{url}" width = "60px" height = "50px"/>'.format(
            url = obj.profile_picture.url,
             )
        )

    profile.short_description = 'Profile  Picture'

admin.site.register(models.Church_Member, ChurchLeadersAdmin)

#Family Representation

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'inspiration', 'profile')
    search_fields = ['family_name']
    fieldsets = [
        ('Family Name', {'fields': ['family_name']}), 
        ('Family Inspiration', {'fields': ['inspiration']}),
        (None, {'fields': ['family_profile']}) 
             
    ]

    def profile(self, obj):
        return mark_safe('<img src = "{url}" width = "50px" height = "50px"/>'.format(
            url = obj.family_profile.url,
             )
        )

    profile.short_description = 'Profile  Picture'

admin.site.register(models.Family, FamilyAdmin)

 

# This is the admin interface for the theme Comment and setting it to be visible
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
    search_fields = ['Scripture_title']
    list_display = ('scripture_title',  'attached_verses' , 'user_id', 'status', 'was_published_recently')
    actions = ['make_invisible', 'make_visible']
    autocomplete_fields = ['user_id']

    # This action is used to show change the state of the
    #  Scripture content and so as to make it more
    #  accessible and also readable

    def make_invisible(self, request, queryset):
        rowsupdated = queryset.update(status = "Invisible")
        if(rowsupdated == 1):
            message_bit = "1 Scripture Was"
        else:
            message_bit = "%s Scriptures Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked Invisible" %message_bit)

    make_invisible.short_description = "Mark the Selected Scripture as Invisible"

    def make_visible(self, request, queryset):
        rowsupdated = queryset.update(status = "visible")
        if(rowsupdated == 1):
            message_bit = "1 Scripture Was"
        else:
            message_bit = "%s Scriptures Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked visible" %message_bit)
        
    make_visible.short_description = "Mark the Selected Scriptures as visible"

admin.site.register(models.Scripture, Scripture)



# The class that handles all the event schedules alongside with their respective updates
class Event(admin.ModelAdmin):
    def profile(self, obj):
        return mark_safe('<img src = "{url}" width = "50px" height = "50px"/>'.format(
            url = obj.image_link.url,
             )
        )

    fieldsets = [
        ("Event Name", {'fields': ['event_name']}), 
        ("Description", {'fields': ['description']}),
        ("Image Link", {'fields': ['image_link']}),
        ("TimeLine", {'fields': ['start_date']}),
        (None, {'fields': ['due_date']}),
        ("Family Responsible", {'fields': ['family_id']})
        
         ]

    profile.short_description = 'Profile  Picture'

    #this returns the the title family responsible and the name in uppercase
    def family_name(self, obj):
        return ("%s" % (obj.family_id)).upper()


    family_name.short_description='Family Responsible'

    list_filter = ['pub_date', 'due_date', 'event_name']
    search_fields = ['event_name']
    list_display = ('event_name', 'start_date','due_date', 'is_date_due', 'family_name', 'was_published_recently', 'profile' )
    inlines = [detailInline]
    
admin.site.register(models.Event, Event)


# The class that handles all the services in the church alongside with their respective updates
class services(admin.ModelAdmin):
    fieldsets = [
        ("Service Name", {'fields': ['service_name']}), 
        ("Description", {'fields': ['description']}),
        ("Image Link", {'fields': ['image_link']}),
        ("Service Day", {'fields': ['day']}),
        ("Service Time", {'fields': ['Time_From']}),
        (None, {'fields':['Time_To']}),
        (None, {'fields':['Venue']}),
        (None, {'fields':['TimeLIne']})
        
         ]


    #this returns the the title family responsible and the name in uppercase
    def family_name(self, obj):
        return ("%s" % (obj.family_id)).upper()


    family_name.short_description='Family Responsible'

    list_filter = ['pub_date','day','service_name']
    search_fields = ['service_name']
    list_display = ('service_name', 'day', 'Venue','Time_From', 'Time_To', 'was_published_recently')
    
admin.site.register(models.services, services)


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
    autocomplete_fields = ['user_id']

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

#This is the sermons model where the sermon and the sermon link is posted through to the users of the website
class sermon(admin.ModelAdmin):
    fieldsets = [
        ('Enter The Details Of The Sermon', {'fields':['sermon_title']}),
        (None, {'fields' :['sermon_speaker']}),
        (None, {'fields' : ['sermon_link']}),
        (None, {'fields': ['sermon_info']})
    ]
    list_filter = ['publication_date']
    search_fields = ['sermon_title', 'sermon_speaker']
    list_display = ['sermon_title', 'sermon_speaker', 'sermon_link', 'was_published_recently']

admin.site.register(models.Sermons, sermon)

#This is the comments in the admin that is placed by the user on the sermon or the other comment
class comments(admin.ModelAdmin):
    fieldsets = [
        ('Sermon Commented On', {'fields': ['sermon']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['comment']}),
        ('Commented By', {'fields': ['comment_by']})
    ]
    list_filter = ['sermon', 'state','comment_by']
    search_fields = ['sermon__sermon_title', 'comment_by']
    list_display = ['sermon', 'state', 'comment_by']
    actions = ['make_invisible', 'make_visible']

    def make_invisible(self, request, queryset):
        rowsupdated = queryset.update(state = False)
        if(rowsupdated == 1):
            message_bit = "1 Comment Was"
        else:
            message_bit = "%s Comments Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked Invisible" %message_bit)

    make_invisible.short_description = "Mark the Selected Comment as Invisible"

    def make_visible(self, request, queryset):
        rowsupdated = queryset.update(state = True)
        if(rowsupdated == 1):
            message_bit = "1 Comment Was"
        else:
            message_bit = "%s Comments Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked visible" %message_bit)
        
    make_visible.short_description = "Mark the Selected Comments as visible"

admin.site.register(models.Comments, comments)

#Admin representation of the details of the contact
class contact(admin.ModelAdmin):
    fieldsets = [
        ('Edit What Appears in The Contact Page', {'fields': ['title']}),
        (None, {'fields':['content']}),        
        ('Enter The Address Details', {'fields': ['Name']}), 
        (None, {'fields': ['name_explain']}),
        (None, {'fields': ['address']}), 
        (None, {'fields': ['email']}),
        (None, {'fields': ['contact']}),
        (None, {'fields': ['timing']})        
    ]

    list_filter = ['pub_date']
    search_fields = ['email']
    list_display = ['title', 'Name','name_explain', 'address', 'email', 'contact', 'timing']

admin.site.register(models.contact, contact)

#Admin representation of the contacts that were sent to the users
class Personal_Contact(admin.ModelAdmin):
    fieldsets = [
        ('The Contacts Sent', {'fields': ['Name']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['contact']}),
        (None, {'fields': ['message']}),
        (None, {'fields': ['status']})
    ]

    list_filter = ['pub_date']
    search_fields = ['Name']
    list_display = ['Name', 'email', 'contact', 'status', 'was_published_recently']
    actions = ['make_viewed']
    readonly_fields = ('Name', 'email', 'contact', 'was_published_recently', 'message')

    #the function that handles the change in status of the message
    def make_viewed(self, request, queryset):
        rowsupdated = queryset.update(status = True)
        if(rowsupdated == 1):
            message_bit = "1 Contact Was"
        else:
            message_bit = "%s Contacts Were " %rowsupdated

        self.message_user(request, "%s Succesfully Marked Viewed" %message_bit)

    make_viewed.short_description = "Mark the Selected Contact as Viewed"


admin.site.register(models.Personal_Contact, Personal_Contact )
# Register your models here.


# The class that handles all the timeline schedules alongside with their respective updates
class Timeline(admin.ModelAdmin):
    fieldsets = [
        ("Event Name", {'fields': ['event_name']}),
        ("TimeLine", {'fields': ['start_date']}),
        (None, {'fields': ['due_date']}),
        ('Is The event Allocated a Sabbath?', {'fields':['is_sabbath']})        
         ]


    #this returns the the title family responsible and the name in uppercase
    def family_name(self, obj):
        return ("%s" % (obj.family_id)).upper()


    family_name.short_description='Family Responsible'

    list_filter = ['pub_date', 'due_date', 'event_name']
    search_fields = ['event_name']
    list_display = ('event_name', 'start_date','due_date', 'is_date_due', 'is_sabbath', 'was_published_recently')
    
admin.site.register(models.Timeline, Timeline)


#This is the registration of the elders and their roles
class Elders(admin.ModelAdmin):
    fieldsets = [
        ('The Elder', {'fields': ['user_id']}),
        ("Is the Elder On Duty?", {'fields' : ['duty']}),
        (None, {'fields': ['short_sharing']}),
        ("Is the Elder Working?", {'fields':['is_working']})
    ]
    list_filter = ['duty', 'is_working']
    list_display = ['user_id', 'duty', 'is_working']

admin.site.register(models.elder, Elders)