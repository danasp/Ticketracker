 # -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import Ticket, TicketComment
from django.db.models import F

STATUS_CHOICE = Ticket.STATUS_CHOICE

# Add new ticket form
class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ['open_date', 'close_date', 'author', 'status', 'classification']
        
# Change status ticket form
class ChangeStatusTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['status', 'classification',]
            
    
# Output filetr tickets form /Tickets/all
class FilterStatusTicketsForm(forms.Form):
    STATUS_CHOICE = (('all','Все'),) + Ticket.STATUS_CHOICE
    status = forms.ChoiceField(choices = STATUS_CHOICE)
        
# Add ticket comment form
class TicketCommentForm(ModelForm):
    class Meta:
        model = TicketComment
        fields = ['body',]
        

        
    
