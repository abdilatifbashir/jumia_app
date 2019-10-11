import csv
from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *
from django.contrib import messages
from django.db.models import Sum
from tablib import  Dataset
from . resources import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='account:login')
def prod(request):
    product = Product.objects.all().order_by('-id')
    # sum = Product.objects.aggregate(Sum('total'))

    return render(request,'product.html',{'product':product,'sum':sum})
    # return HttpResponse('God help us here')

@login_required
def new_product(request):
    # current_user = request.user
    if request.method == 'POST':
        form = NewProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = Product()
            product.item = form.cleaned_data['item']
            product.category = form.cleaned_data['category']
            product.sub_category = form.cleaned_data['sub_category']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.save()
            messages.success(request,'product added successfuly')
            return redirect('prod')

    else:
        form= NewProductForm()

    return render(request, 'new_product.html', {'form':form})



def export(request):
    '''
    eport to csv file
    '''
    product_resource = ProductResource()
    # queryset = Product.objects.filter(cat='tv')#for manupulation and pass queryset as agurment of expoert
    dataset = product_resource.export()
    response = HttpResponse(dataset.csv,content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    return response


def export_exel(request):
    '''
    export to spreadsheet file
    '''
    product_resource = ProductResource()
    # queryset = Product.objects.filter(product='Chelsea')#for manupulation and pass queryset as agurment of expoert
    dataset = product_resource.export()
    response = HttpResponse(dataset.csv,content_type='application/vnd.ms-exel')
    response['Content-Disposition'] = 'attachment; filename="product.xls"'
    return response



def export_product_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'

    writer = csv.writer(response)
    writer.writerow(['Item', 'Category', 'Sub_category', 'Price per unit','Quantity','Shipping cost','Commision',])

    product = Product.objects.all().values_list('item', 'category', 'sub_category', 'price','quantity','shipping','commision')
    for p in product:
        writer.writerow(p)

    return response


def clear_data(request):
    data = Product.objects.all()
    data.delete()
    return redirect('prod')
