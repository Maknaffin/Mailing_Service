from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import BaseTemplateView, MailingsListView, MailingsCreateView, MailingsUpdateView, \
    MailingsDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('list/', MailingsListView.as_view(), name='mailing_list'),
    path('create/', MailingsCreateView.as_view(), name='mailing_create'),
    path('edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailing_edit'),
    path('delete/<int:pk>/', MailingsDeleteView.as_view(), name='mailing_delete'),
]
