from django import forms
from django.core.exceptions import ValidationError


class ImageUploadForm(forms.Form):
    image = forms.ImageField(required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        check = [self.cleaned_data['image'], self.cleaned_data['text']]
        if any(check) and not all(check):
            return self.cleaned_data
        raise ValidationError('Select either image or text')
