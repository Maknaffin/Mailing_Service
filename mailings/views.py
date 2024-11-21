from django.views.generic import TemplateView, ListView

from mailings.models import Mailings


class BaseTemplateView(TemplateView):
    template_name = 'mailings/base.html'


class MailingsListView(ListView):
    model = Mailings
