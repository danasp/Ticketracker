 # -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       
    url (r'^all/$', 'ticketracker.views.all_tickets', name = 'ticketracker_all_tickets'),
    url (r'^get/(?P<ticket_id>\d+)/$', 'ticketracker.views.get_ticket'),
    url (r'^change_ticket/(?P<ticket_id>\d+)/$', 'ticketracker.views.get_ticket'),
    url (r'^add_ticket/$', 'ticketracker.views.add_ticket'),
    url (r'^add_comment/(?P<ticket_id>\d+)/$', 'ticketracker.views.add_comment'),
    
                       
)