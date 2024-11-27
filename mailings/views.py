from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingForm, MessageForm
from mailings.models import Mailings, Message


class BaseTemplateView(TemplateView):
    template_name = 'mailings/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_active'] = 0
        return context


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

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     MessageFormset = inlineformset_factory(Mailings, Message, form=MessageForm, extra=1)
    #     context_data['formset'] = MessageFormset()
    #
    #     # if self.request.method == 'POST':
    #     #     context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
    #     # else:
    #     #     context_data['formset'] = MessageFormset(instance=self.object)
    #     return context_data



class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')
