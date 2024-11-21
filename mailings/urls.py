from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import BaseTemplateView, MailingsListView

app_name = MailingsConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('list/', MailingsListView.as_view(), name='mailing_list'),
]
