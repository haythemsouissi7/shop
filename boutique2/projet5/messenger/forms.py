from django.forms import ModelForm
from messenger.models import Message,Attache


class AttacheForm(ModelForm):
  class Meta:
    model = Attache
    fields = ['image']