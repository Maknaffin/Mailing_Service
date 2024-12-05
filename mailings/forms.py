from django import forms

from mailings.models import Mailings, Message, Clients


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Mailings
        fields = '__all__'


class MessageForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
