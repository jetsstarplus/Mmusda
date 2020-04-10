from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
    choice = [
        ('Members Welfare', 'Members Welfare'),
        ('Internal Activities', 'Internal Activities'),
        ('Church Affairs', 'Church Affairs'),
        ('Ministry & Outreach', 'Ministry & Outreach')
    ]

    department_name = models.CharField(max_length = 20)
    department_role = models.CharField(max_length = 500)
    department_inspiration = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, choices = choice, blank = True)
   

    def __str__(self):
        return self.department_name


class Church_Member(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    contact = models.CharField(max_length = 20)
    Adm_Year = models.IntegerField('Year Of Admission')


    # a concatenation of the first name and the last name
    def full_names(self):
        return self.user.first_name + ' ' + self.user.last_name

    full_names.short_description = 'Full Name'
    full_names.admin_order_field = 'leader_last_name'

    full_name = property(full_names)

    def __str__(self):
       
        return self.full_name
        
    class Meta:
        verbose_name_plural = 'Church Members'
    


class Announcement(models.Model):
    status_choice = [
        ('Announcement', 'Announcement'),
        ('Sub-Announcement', 'Sub-Announcement')
    ]
    announcement_title = models.CharField(max_length = 30)
    announcement_description = models.TextField()
    announcement_due_date = models.DateTimeField('Due Date')
    publication_date = models.DateTimeField('Date Published', default = timezone.now())
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)
    announcement_classification = models.CharField(max_length = 30, choices = status_choice)
    announcement_specification = models.CharField(max_length = 100, default = "None")

    def __str__(self):
        return self.announcement_title

        #check if indeed the date is due
    def is_date_due(self):
        now = timezone.now()
        return now-datetime.timedelta(days = 14) <= self.announcement_due_date >= now
    

    #justification if the date was indeed due
    is_date_due.admin_order_field = "due_date"
    is_date_due.boolean = True
    is_date_due.short_description = 'Is Due'

    #check if it was recently published
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.publication_date <= now

    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    # The theme Scripture model
class Scripture(models.Model):
    status_choice = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]
    scripture_title = models.CharField(max_length = 30)
    scripture_content = models.TextField()
    attached_verses = models.CharField(max_length = 30)
    pub_date = models.DateTimeField('Date published', default = timezone.now())
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = status_choice)

    def __str__(self):
        return self.scripture_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now

    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Family(models.Model):
    FAMILY_NAMES = [
        ('Emeralds', 'Emeralds'),
        ('Heralds', 'Heralds'),
        ('Humble', 'Humble'),
        ('Aroma', 'Aroma'),
        ('Pilgrims', 'Pilgrims'),
        ('Royals', 'Royals'),
        ('Eagles', 'Eagles'),
        ('All', 'All')
    ]
    family_name = models.CharField(max_length = 20, choices = FAMILY_NAMES)
    #family_announcements = models.ForeignKey(Announcements, on_delete = models.CASCADE)
    inspiration = models.CharField(max_length = 500)

    
    class Meta:
        verbose_name_plural = 'Families'

    def __str__(self):
        return self.family_name



class Event(models.Model):
   
    event_name = models.CharField(max_length= 50)
    start_date = models.DateTimeField('Start Date')
    due_date = models.DateTimeField('Due Date', blank = True)
    description = models.TextField()
    image_link = models.ImageField(upload_to = 'sda')
    pub_date = models.DateTimeField('Publication Date', default = timezone.now())
    family_id = models.ForeignKey(Family, on_delete = models.CASCADE)

    def __str__(self):
        return self.event_name
    
    def timeSpan(self):
        return self.due_date - self.start_date <= datetime.timedelta(days = 1)

    #check if the publication was done recently
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now

    #check if indeed the date is due
    def is_date_due(self):
        now = timezone.now()
        return now-datetime.timedelta(days = 14) <= self.due_date >= now
    
    #the timespan function justification
    timeSpan.boolean = True

    #justification if the date was indeed due
    is_date_due.admin_order_field = "due_date"
    is_date_due.boolean = True
    is_date_due.short_description = 'Is Due'

    #justifications to confirm if publication was recent    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class services(models.Model):
    choice = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Teusday', 'Teusday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thusday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    ]

    timeChoice = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening')
    ]
   
    service_name = models.CharField(max_length= 50)
    description = models.TextField()
    image_link = models.ImageField(upload_to = 'services')
    pub_date = models.DateTimeField('Publication Date', default = timezone.now())
    day = models.CharField(blank = True, choices = choice, max_length = 50)
    Time_From = models.TimeField(blank = True)
    Time_To = models.TimeField(blank = True)
    Venue = models.CharField(blank = True, max_length = 50)
    TimeLIne = models.CharField(blank = True, max_length = 50, choices = timeChoice)
    
    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_name

    #check if the publication was done recently
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now

    
    def timeSpan(self):
        span = self.Time_To - self.Time_To
        return span
    

    #justifications to confirm if publication was recent    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# this model holds the details of the events described above
class EventsDetail(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    sub_title = models.CharField(max_length = 50)
    detail = models.CharField(max_length = 200)
    
   
    def __str__(self):
        return self.sub_title


class visitor_word(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now())
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Visitor Word'

    def __str__(self):
        return self.title 

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class About(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now())
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)

    
    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title 

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


#This is the model for other Businesses as displayed in the Home Page
class OtherBussiness(models.Model):
    other_title = models.CharField(max_length = 30)
    other_description = models.TextField()
    pub_date = models.DateTimeField('Date Published', default = timezone.now())
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Other Businesses'

    def __str__(self):
        return self.other_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class elder(models.Model):
    user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)
    duty = models.BooleanField('Is Elder On Duty')
    short_sharing = models.TextField()
    is_working = models.BooleanField('Is Elder Active')



class Leaders_Department(models.Model):
                                                                                        
        DEPARTMENTS = [
            ('hod', 'Head Of Department'),
            ('hod1','Assistant Head'),
            ('hod2', 'Second Assistant'),
            ('hod3','Third Assistant')
        
        ]


        user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)
        dept_id = models.ForeignKey(Department, on_delete = models.CASCADE)
        dpt_role = models.CharField(max_length = 30, choices = DEPARTMENTS, default = 'Family')
        dpt_rate = models.IntegerField()

        class Meta:
            verbose_name_plural = 'Department Leaders'



class Leaders_Family(models.Model):
        FAMILY = [
            ('mom','Family Mom'),
            ('dad','Family Dad'),
            ('Child', 'Child')
            
        ]

        user_id = models.ForeignKey(Church_Member, on_delete = models.CASCADE)
        family = models.ForeignKey(Family, on_delete = models.CASCADE)
        fam_role = models.CharField(max_length = 30, choices = FAMILY, default = 'Child')




#The Most Frequently asked Questions Models that are to stored in the database
class faq(models.Model):
    question = models.CharField(max_length = 200)
    answer = models.TextField()
    pub_date = models.DateTimeField("Date Published", default = timezone.now())

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 7) <=  self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# Create your models here.


