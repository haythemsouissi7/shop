from __future__ import unicode_literals

import os
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from produit.models import Produit
def get_message(instance, filename):
    return os.path.join(instance.message.user.username, 'messages', '{}_{}'.format('message', instance.message.date.__format__('%b_%m _%H_%m')), '{}_{}'.format('image', timezone.now()))

@python_2_unicode_compatible
class Message(models.Model):
    user = models.ForeignKey(User, related_name='+')
    message = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(User, related_name='+')
    from_user = models.ForeignKey(User, related_name='+')
    is_read = models.BooleanField(default=False)
    objet=models.CharField(max_length=250,null=True)
    produit=models.ForeignKey(Produit,null=True)
    
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ('date',)
        db_table = 'messages_message'

    def __str__(self):
        return self.message

    @staticmethod
    def send_message(from_user, to_user, message,objet,produit):
        
        current_user_message = Message(from_user=from_user,
                                       message=message,
                                       user=from_user,
                                       conversation=to_user,
                                       objet=objet,
                                       produit=produit,
                                       is_read=True)
        current_user_message.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                objet=objet,
                produit=produit,
                user=to_user).save()

        return current_user_message


    
    @staticmethod
    def get_conversations(user):
        conversations = Message.objects.filter(
            user=user).values('conversation').annotate(
                last=Max('date')).order_by('-last')
        users = []
        for conversation in conversations:
            users.append({
                'user': User.objects.get(pk=conversation['conversation']),
                'last': conversation['last'],
                'unread': Message.objects.filter(user=user,
                                                 conversation__pk=conversation[
                                                    'conversation'],
                                                 is_read=False).count(),
                })

        return users

class Attache(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_message)

