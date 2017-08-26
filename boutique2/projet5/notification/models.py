from django.db import models

import os

from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from produit.models import Produit


from django.db import models

import json

from django.db.models.functions import TruncMonth, TruncDay
from django.db.models import Count

from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from produit.models import Produit

# Create your models here.


class Notification(models.Model):
    NORMAL = 'normal'
    SMILE = 'smile'
    LOVE = 'love'
    WISH = 'wish'

    NOTIFICATION_TYPES = (
        (NORMAL, 'normal'),
        (SMILE, 'smile'),
        (LOVE, 'love'),
        (WISH, 'wish'),
    )


    _NORMAL_TEMPLATE = '<a href="/settings/{0}/">{1}</a> has reacted normal to your product: <a href="/boutique/vosproduit/{2}/">{3}</a>'  # noqa: E501
    _SMILE_TEMPLATE = '<a href="/settings/{0}/">{1}</a> has reacted with smile to your product: <a href="/boutique/vosproduit/{2}/">{3}</a>'  # noqa: E501
    _LOVE_TEMPLATE = '<a href="/settings/{0}/">{1}</a> loves your product: <a href="/boutique/vosproduit/{2}/">{3}</a>'  # noqa: E501
    _WISH_TEMPLATE = '<a href="/settings/{0}/">{1}</a> wishes your product: <a href="/boutique/vosproduit/{2}/">{3}</a>'  # noqa: E501



    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    product = models.ForeignKey(Produit, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        if self.type == self.NORMAL:
            return self._NORMAL_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.title))
                )
        elif self.type == self.SMILE:
            return self._SMILE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.title))
                )
        elif self.type == self.LOVE:
            return self._LOVE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.title))
                )
        elif self.type == self.WISH:
            return self._WISH_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.title))
                )
        
        else:
            return 'Ooops! Something went wrong.'

    def get_summary(self, value):
        summary_size = 50
        if len(value) > summary_size:
            return '{0}...'.format(value[:summary_size])

        else:
            return value
    

    def send(from_user, to_user, product, type):
        notification = Notification(from_user=from_user,
                                    to_user=to_user,
                                    product=product,
                                    type=type).save()
        return notification