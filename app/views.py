import csv
import xlwt
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
    current_user = request.user
    product = Product.objects.filter(vendor=current_user).order_by('-id')
    sum = Product.objects.filter(vendor=current_user).aggregate(Sum('amount_expected'))
    return render(request,'product.html',{'product':product,'sum':sum})
    # return HttpResponse('God help us here')

@login_required
def new_product(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = Product()
            product.item = form.cleaned_data['item']
            product.category = form.cleaned_data['category']
            product.sub_category = form.cleaned_data['sub_category']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.vendor = current_user
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
    '''
    manual way to cssv
    '''
    current_user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    items = Product.objects.filter(vendor=current_user).order_by('-id')
    writer = csv.writer(response)
    writer.writerow(['Item', 'Category', 'Sub_category', 'Price per unit','Quantity','Shipping cost','Commision',])


    for obj in items:
        writer.writerow([obj.item,obj.category,obj.sub_category,obj.price,obj.quantity,obj.shipping,obj.commision])

    return response


def clear_data(request):
    current_user = request.user
    data = Product.objects.filter(vendor=current_user)
    data.delete()
    return redirect('prod')




def pload(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

    return render(request, "upload.html", locals())
