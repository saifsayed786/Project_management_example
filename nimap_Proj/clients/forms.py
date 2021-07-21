from django.forms import ModelForm

from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields= '__all__'
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'