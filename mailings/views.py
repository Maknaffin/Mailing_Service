from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingForm, MessageForm, ClientForm
from mailings.models import Mailings, Message, Clients, Logs
from mailings.services import set_period


class BaseTemplateView(TemplateView):
    template_name = 'mailings/statistics.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['full_list'] = Mailings.objects.filter(mailing_owner=self.request.user).count()
        context_data['full_list'] = Mailings.objects.all().count()
        # context_data['active_list'] = Mailings.objects.filter(is_active=True, mailing_owner=self.request.user).count()
        context_data['active_list'] = Mailings.objects.all().count()
        # context_data['count_clients'] = Clients.objects.filter(client_owner=self.request.user).count()
        context_data['count_clients'] = Clients.objects.all().count()
        return context_data


class MailingsListView(LoginRequiredMixin, ListView):
    model = Mailings
    # permission_required = 'mailings.view_mailings'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(mailing_owner=self.request.user)
        return queryset


class MailingsCreateView(CreateView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MailingForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.mailing_owner = self.request.user
        self.object.next_try = set_period()
        self.object.save()
        return super().form_valid(form)


class MailingsUpdateView(UpdateView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')
    form_class = MailingForm

    def form_valid(self, form):
        self.object = form.save()
        self.model.mailing_status = self.object.mailing_status
        self.object.mailing_owner = self.request.user
        self.object.next_try = set_period()
        self.object.save()
        return super().form_valid(form)


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(message_owner=self.request.user)
        return queryset


class MessageCreateView(CreateView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')
    form_class = MessageForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.message_owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')
    form_class = MessageForm


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Clients

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(client_owner=self.request.user)
        return queryset


class ClientCreateView(CreateView):
    model = Clients
    success_url = reverse_lazy('mailings:client_list')
    form_class = ClientForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.client_owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Clients
    success_url = reverse_lazy('mailings:client_list')
    form_class = ClientForm


class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('mailings:client_list')


class LogListView(LoginRequiredMixin, ListView):
    model = Logs

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(logs_owner=self.request.user)
        return queryset
