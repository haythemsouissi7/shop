from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import Promotion
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404


@task(name="sum_two_numbers")
def add(x, y):
    return x + y




@task(name="active_promotion")
def activate(a):
	print("anis hachani")
	promotion=get_object_or_404(Promotion,pk=a)
	promotion.is_active=True
	promotion.start=promotion.start
	promotion.end=promotion.end
	promotion.save()
	return promotion.is_active

@task(name="desactive")
def desactivate(a):
	promotion=get_object_or_404(Promotion,pk=a)
	promotion.is_active=False
	promotion.start=promotion.start
	promotion.end=promotion.end
	promotion.save()
	return promotion.is_active
