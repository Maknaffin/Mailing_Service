from django import forms

from mailings.models import Mailings, Message


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'