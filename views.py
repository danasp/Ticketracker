 # -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ticket, TicketComment
from .forms import TicketForm, TicketCommentForm, ChangeStatusTicketForm, FilterStatusTicketsForm
from django.core.context_processors import csrf
from django.utils import timezone


def all_tickets(request):
    tickets = Ticket.objects.order_by('-open_date')
    if request.method == 'POST':
        status_form = FilterStatusTicketsForm(request.POST)
        if status_form.is_valid():
            tickets = Ticket.objects.filter(
                status=status_form.cleaned_data['status']
                ).order_by(
                '-open_date'
                )
            if status_form.cleaned_data['status'] == 'all':
                tickets = Ticket.objects.order_by('-open_date')
            
    args = {}
    args.update(csrf(request))
    args['status_form'] = FilterStatusTicketsForm()
    args['tickets'] = tickets
    args['user']=request.user
    return render_to_response('all_tickets.html', args)

def get_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = ChangeStatusTicketForm(request.POST)
        if form.is_valid():
            ticket.status = form.cleaned_data['status']
            if ticket.status == 'c':
                ticket.close_date = timezone.now()
            ticket.classification = form.cleaned_data['classification']
            ticket.save()
            return HttpResponseRedirect ('/tickets/all')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = ChangeStatusTicketForm(instance=ticket)
        args['ticket'] = ticket
        return render_to_response('get_ticket.html', args)
       
def add_ticket(request):
    if request.method == "POST":
        pre_form = TicketForm(request.POST, request.FILES)
        
        if pre_form.is_valid():
            form = pre_form.save(commit=False)
            # Add author_oi to ticket. Aythor should be authorised
            form.author_id = request.user.id
            form.save()
            return HttpResponseRedirect('/tickets/all')
        else:
            return ('Не верно заполнены поля.')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = TicketForm()
        return render_to_response('add_ticket.html', args)
    
def add_comment(request, ticket_id):
    tt = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        pre_form = TicketCommentForm(request.POST)
        if pre_form.is_valid():
            form = pre_form.save(commit=False)
            form.author_id = request.user.id
            form.pub_date = timezone.now()
            form.ticket = tt
            form.save()
            return HttpResponseRedirect('/tickets/get/%s' % ticket_id)
    else:
        args={}
        args.update(csrf(request))
        args['ticket'] = tt
        args['form'] = TicketCommentForm()
        return render_to_response('add_ticket_comment.html', args)
