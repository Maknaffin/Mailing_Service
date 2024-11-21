from django.contrib import admin

from mailings.models import Message, Clients, Mailings


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'message_owner',)


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'full_name', 'comments', 'client_owner',)


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('mailing_name', 'mailing_start', 'mailing_finish', 'next_try', 'period', 'status',
                    'mailing_owner', 'mail_title', 'is_active')
