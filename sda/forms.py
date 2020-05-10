from django.forms import ModelForm, Textarea, TextInput
from . import models

class Contact(ModelForm):
    class Meta:
        model = models.Personal_Contact
        fields = ['Name', 'email', 'contact', 'message']
        widgets = {
            'contact': TextInput(attrs = {'rows':2}), 
            'message': Textarea(attrs = {'cols': 80, 'rows':6, 'class':'form-control', 'id':'input4'})
        }
