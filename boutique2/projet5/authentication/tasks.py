from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from promotion.models import Promotion
from datetime import datetime, timedelta



@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)


@task(name="active_promotion")
def activate(a):
	print("anis hachani")
	promotion=Promotion.objects.get(pk=a)
	promotion.is_active=True
	promotion.save()
	return promotion.is_active

@task(name="desactive")
def desactivate(a):
	promotion=Promotion.objects.get(pk=a)
	promotion.is_active=False
	promotion.save()
	return promotion.is_active
