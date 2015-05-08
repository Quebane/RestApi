from django import forms
from djangular.forms import NgModelFormMixin, NgForm


class ImageForm(NgModelFormMixin, NgForm):
    url = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))