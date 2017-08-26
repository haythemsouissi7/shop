from django import forms
from django.contrib.auth.models import User

from .models import Collection




class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ['title', 'discription','picture','produit' ]



