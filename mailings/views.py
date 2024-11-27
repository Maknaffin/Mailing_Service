from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingForm, MessageForm
from mailings.models import Mailings, Message


class BaseTemplateView(TemplateView):
    template_name = 'mailings/base.html'


class MailingsListView(ListView):
    model = Mailings


class MailingsCreateView(CreateView):
    model = Mailings
    # fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MailingForm


class MailingsUpdateView(UpdateView):
    model = Mailings
    # fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MailingForm


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    # fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MessageForm


class MessageUpdateView(UpdateView):
    model = Message
    # fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MessageForm


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:mailing_list')
