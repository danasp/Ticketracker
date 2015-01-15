 # -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Ticket, TicketComment
from django.utils import timezone

class TicketCommentAdmin(admin.TabularInline):
    readonly_fields = ('author', 'body')
    model = TicketComment
    extra = 0
    can_delete = False


class TicketAdmin (admin.ModelAdmin):
    
    actions = ['close_tickets']
    
    def close_tickets(self, request, queryset):
        queryset.update(status='c')
        queryset.update(close_date = timezone.now())
    close_tickets.short_description = "Mark selected ticket as closed" 
    
    #fields = ['author', 'author_email' ,'title', 'body', 'status']
        
    fieldsets = [
        (None, {
            'fields':['author','author_email']
        }),
        ('Context', {
            'classes': ['extrapretty',], 
            'fields': ['title', 'body', 'upload_file']
        }),
        (None, {
            'fields':['status', 'classification']
        }),
    ]
    
    inlines = [TicketCommentAdmin, ]
    
    list_display = ('title', 'open_date', 'does_close_date', 'is_ticket_open')
    
    list_display_links = ('title', 'open_date', 'does_close_date', 'is_ticket_open')
    
    list_filter = ('open_date', 'close_date')
    #list_editable  = ()
    search_fields = ['title', 'body']
    
    list_per_page = 25
    
admin.site.register(Ticket, TicketAdmin)