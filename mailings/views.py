from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingForm, MessageForm, ClientForm
from mailings.models import Mailings, Message, Clients


class BaseTemplateView(TemplateView):
    template_name = 'mailings/statistics.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['full_list'] = Mailings.objects.all().count()
        context_data['active_list'] = Mailings.objects.filter(is_active=True).count()
        context_data['unique_clients_list'] = Clients.objects.all().count()
        return context_data


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
    success_url = reverse_lazy('mailings:message_list')
    form_class = MessageForm


class MessageUpdateView(UpdateView):
    model = Message
    # fields = '__all__'
    success_url = reverse_lazy('mailings:message_list')
    form_class = MessageForm


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class ClientListView(ListView):
    model = Clients


class ClientCreateView(CreateView):
    model = Clients
    # fields = '__all__'
    success_url = reverse_lazy('mailings:client_list')
    form_class = ClientForm


class ClientUpdateView(UpdateView):
    model = Clients
    # fields = '__all__'
    success_url = reverse_lazy('mailings:client_list')
    form_class = ClientForm


class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('mailings:client_list')
