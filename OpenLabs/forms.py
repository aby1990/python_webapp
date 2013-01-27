from django.forms import ModelForm
from OpenLabs.models import details

class detailsForm(ModelForm):
    class Meta:
        model = details