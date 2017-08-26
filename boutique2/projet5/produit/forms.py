from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, FileInput, Select, CheckboxInput
from .models import Boutique, Produit


class BoutiqueForm(forms.ModelForm):

    class Meta:
        model = Boutique
        fields = ['name', 'logo']


class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = ['prix', 'title', 'descreption', 'type', 'etat', 'categorie','logo', 'image1' , 'image2', 'image3', 'quantite']










