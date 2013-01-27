from django.db import models
#from django.forms import ModelForm
#from django.contrib.auth.models import User

#QUAL_CHOICES = (
#    ('High School', 'Secondary School'),
#    ('Bachelors', 'Masters'),
#)

class details(models.Model):
    name = models.CharField(max_length=30)
    bdate = models.DateField();
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.IntegerField(max_length=10)
    qual = models.CharField(max_length=15)
    skill = models.CharField(max_length=60)

def _unicode_(self):
    return self.name

#class detailsForm(ModelForm):
#    class Meta:
#        model = details