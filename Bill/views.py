from django.shortcuts import render
from .models import Product_Bill
from .models import Service_Bill

# Create your views here.
def ShowProduct_Bill(request):
    Product_Bill_List= Product_Bill.objects.all()
    context = {'Product_Bill_List': Product_Bill_List}

    return render( request,'Bill/Product_BillList.html',context)



def ShowService_Bill(request):
    Service_Bill_List = Service_Bill.objects.all()
    context = {'Service_Bill_List': Service_Bill_List}

    return render( request,'Bill/Service_BillList.html',context)


