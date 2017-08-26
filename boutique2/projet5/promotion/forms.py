from django import forms
from django.contrib.auth.models import User

from .models import Promotion




class PromotionForm(forms.ModelForm):

    class Meta:
        model = Promotion
        fields = ['start','end' ]


class promotionstartform(forms.ModelForm):
	class Meta:
		model = Promotion
		fields = ['start' ]

