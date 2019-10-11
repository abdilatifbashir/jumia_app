from django import forms
from .models import Product, Sub_category, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['total','commision']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = Sub_category.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['sub_category'].queryset = Sub_category.objects.filter(category_id=category_id).order_by('id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.sub_category_set.order_by('id')
