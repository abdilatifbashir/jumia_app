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
import pandas as pd


# Create your views here.
@login_required(login_url='account:login')
def prod(request):
    product = Product.objects.all().order_by('-id')
    sum = Product.objects.aggregate(Sum('amount_expected'))
    uploaded_files = UploadedFiles.objects.all()

    print(sum)
    return render(request,'product.html',{'product':product,'sum':sum, 'upload': uploaded_files})
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
            product.serial_no = form.cleaned_data['serial_no']
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
    current_user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    items = Product.objects.filter(vendor=current_user).order_by('-id')
    writer = csv.writer(response)
    writer.writerow(['Item', 'Category', 'Sub_category', 'Price per unit', 'Serial Number', 'Shipping cost', 'Commision','Toatl' ])

    for obj in items:
        writer.writerow(
            [obj.item, obj.category, obj.sub_category, obj.price, obj.serial_no, obj.shipping, obj.commision, obj.amount_expected])

    return response


def clear_data(request):
    data = Product.objects.all()
    data.delete()
    return redirect('prod')


def compare_csv_files(request, id):
    csv_files = get_object_or_404(UploadedFiles, id=id)
    file1 = csv_files.file
    file2 = csv_files.file2
    a = pd.read_csv(file1)
    b = pd.read_csv(file2)
    col1 = a['Serial Number']
    col2 = b['Serial Number']
    same_dict = []
    different_dict = []
    same_messages = None
    diff_messages = None
    message1 = None
    message2 = None
    message1_dif = None
    message2_dif = None
    for row1, row2 in zip(col1, col2):
        if row1 == row2:
            values1 = a.loc[a['Serial Number'] == row1, ['Item', 'Toatl']].values[0]

            values2 = b.loc[b['Serial Number'] == row2, ['Item', 'Toatl']].values[0]
            price1 = values1[1]
            price2 = values2[1]
            name_price1 = values1[0]
            name_price2 = values2[0]
            if price1 == price2:
                message1 = name_price1 + " price in system generated file is :  " + str(price1)
                message2 = name_price2 + " price in Jumia Report is :  " + str(price2)
                message1 = str(message1)
                message2 = str(message2)
                same_dict.append(message1)
                same_dict.append(message2)
            else:
                message1_dif = name_price1 + " price in system generated file is : " + str(price1)
                message2_dif = name_price2 + " price in Jumia file is : " + str(price2)
                message1_dif = str(message1_dif)
                message2_dif = str(message2_dif)
                different_dict.append(message1_dif)
                different_dict.append(message2_dif)
    return render(request, 'display.html', {'same': same_dict, 'different': different_dict})




