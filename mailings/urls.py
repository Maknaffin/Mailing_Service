from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import BaseTemplateView, MailingsListView, MailingsCreateView, MailingsUpdateView, \
    MailingsDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, ClientCreateView, \
    ClientListView, ClientUpdateView, ClientDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),

    path('mailing_list/', MailingsListView.as_view(), name='mailing_list'),
    path('mailing_create/', MailingsCreateView.as_view(), name='mailing_create'),
    path('mailing_edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailing_edit'),
    path('mailing_delete/<int:pk>/', MailingsDeleteView.as_view(), name='mailing_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('client_list/', ClientCreateView.as_view(), name='client_create'),
    path('client_create/', ClientListView.as_view(), name='client_list'),
    path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
