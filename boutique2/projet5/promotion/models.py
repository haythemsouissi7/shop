from django.db import models
from collection.models import Collection
from produit.models import Produit
from datetime import datetime
from django.db import models
from django.conf import settings
# Create your models here.
now =datetime.now()
class Promotion(models.Model):
	typechoix = (('flashe', 'flashe'), ('regular', 'regular'),)
	produit=models.ForeignKey(Produit,blank=True,null=True,on_delete=models.CASCADE)
	collection = models.ForeignKey(Collection,on_delete=models.CASCADE,blank=True,null=True)
	created_at=models.DateTimeField(auto_now_add=True, null=True)
	start=models.DateTimeField(null=True)
	end=models.DateTimeField(null=True)
	timestart=models.TimeField(null=True)
	timeend=models.TimeField(null=True)
	promo_type = models.CharField(max_length=250,choices=typechoix, default="vintage")
	types=models.CharField(max_length=1,null=True)
	discount=models.IntegerField(null=True)
	is_active=models.BooleanField(default = False)

	def get_time(self):
		a=self.end.hour -now.hour
		b=self.end.minute - now.minute
		return str(a) +':'+ str(b)
