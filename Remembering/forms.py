from django import forms
from django.core.exceptions import ValidationError

from .models import Person

class ImageUploadForm(forms.Form):
    image = forms.ImageField(required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        if 'image' in self.cleaned_data and 'text' in self.cleaned_data:
            check = [self.cleaned_data['image'], self.cleaned_data['text']]
        else:
            raise ValidationError('Incorrect file format')
        if any(check) and not all(check):
            return self.cleaned_data
        raise ValidationError('Select either image or text')


class NewUserForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'email']
