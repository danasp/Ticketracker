 # -*By- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from time import time

def upload_file_name(instance, filename):
    return 'ticket/%s/%s_%s' % (instance.title,str(time()).replace('.','_'), filename)

class Ticket(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    open_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User)
    author_email = models.EmailField('e-mail')
    upload_file = models.FileField(upload_to = upload_file_name, null=True)
    STATUS_CHOICE = (
        ('o', 'Открыт'),
        ('c', 'Закрыт'),
        ('m', 'Под наблюдением'),
    )
    status = models.CharField(max_length = 1,
                              choices = STATUS_CHOICE,
                              default ='o')
    
    classification = models.BooleanField('Общая проблема', default=False)
    
    def __unicode__(self):
        return self.title
    
    def is_ticket_open(self):
        if self.status == 'o':
            return True
        else:
            return False
    
    def does_close_date(self):
        if self.close_date == None:
            return 'Ticket do not close yet'
        else:
            return self.close_date
    
    is_ticket_open.short_description = 'Is Ticket Open?'
    is_ticket_open.boolean = True
    does_close_date.short_description = "Closed date"
    
class TicketComment(models.Model):
    author = models.ForeignKey(User)
    ticket = models.ForeignKey(Ticket)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    