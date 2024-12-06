from django import forms
from django.forms import DateTimeInput, Select

from mailings.models import Mailings, Message, Clients


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ['status', 'period', 'mail_title', 'client_email']:
                field.widget.attrs['class'] = 'form-select'
            elif field_name == 'is_active':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleMixin, forms.ModelForm):
    mailing_start = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                                        label='Дата и время начала рассылки')
    mailing_finish = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                                         label='Дата и время окончания рассылки')
    next_try = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                                   label='Дата и время следующей попытки')

    class Meta:
        model = Mailings
        exclude = ('mailing_owner',)


class MessageForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('message_owner',)


class ClientForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ('client_owner',)
