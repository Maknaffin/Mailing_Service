from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailings.models import Mailings


class BaseTemplateView(TemplateView):
    template_name = 'mailings/base.html'


class MailingsListView(ListView):
    model = Mailings


class MailingsCreateView(CreateView):
    model = Mailings
    fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')


class MailingsUpdateView(UpdateView):
    model = Mailings
    fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')