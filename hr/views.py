
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product, Sub_category
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_changelist')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_changelist')


def load_sub_categories(request):
    category_id = request.GET.get('category')
    sub_categories = Sub_category.objects.filter(category_id=category_id).order_by('id')
    return render(request, 'hr/sub_category_dropdown_list_options.html', {'sub_categories': sub_categories})
