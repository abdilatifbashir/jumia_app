from django import forms
from .models import *

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['total','commision', 'amount_expected', 'vendor']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ('file',)
