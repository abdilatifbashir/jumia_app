from django import forms
from .models import *
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['total','commision','amount_expected','vendor']
