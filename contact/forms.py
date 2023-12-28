from . import models
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone',


    def clean(self):
       cleaned_data = self.cleaned_data
       first_name = cleaned_data.get('first_name')
       last_name = cleaned_data.get('last_name')

       if first_name == last_name:
        msg = ValidationError(
              "First name can't be equal last name",
                code='invalid',
            )
        self.add_error('first_name', msg)
        self.add_error('last_name', msg)


        return super().clean()