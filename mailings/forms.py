from django import forms
from django.forms import DateTimeInput

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

    class Meta:
        model = Mailings
        exclude = ('mailing_owner', 'mailing_status', 'next_try',)


class MessageForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('message_owner',)


class ClientForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ('client_owner',)
