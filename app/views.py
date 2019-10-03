import csv
from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *
from django.contrib import messages
from django.db.models import Sum


# Create your views here.

def prod(request):
    product = Product.objects.all().order_by('-id')
    sum = Product.objects.aggregate(Sum('total'))

    return render(request,'product.html',{'product':product,'sum':sum})



def new_product(request):
    # current_user = request.user
    if request.method == 'POST':
        form = NewProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = Product()
            product.item_name = form.cleaned_data['item_name']
            product.cat = form.cleaned_data['cat']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.save()
            messages.success(request,'product added successfuly')
            return redirect('prod')

    else:
        form= NewProductForm()

    return render(request, 'new_product.html', {'form':form})



def download_csv(request):
    '''
    function that exports html table to csv
    '''
    items = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Deposition']= 'attachment;filename="product.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['item_name','cat','price','quantity','total'])
    for obj in items:
        writer.writerow([obj.item_name,obj.cat,obj.price,obj.quantity,obj.total])
    return response

def clear_data(request):
    data = Product.objects.all()
    data.delete()
    return redirect('prod')
