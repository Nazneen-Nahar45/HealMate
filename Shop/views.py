from django.shortcuts import render, get_object_or_404
from .models import AddProduct
from .form import orderform
from django.contrib.auth.decorators import login_required


# Create your views here.

def showproduct(request):
    product = AddProduct.objects.all()
    if request.method == 'POST':
        product = AddProduct.objects.filter(Product_name__icontains=request.POST['search'])
        category = AddProduct.objects.filter(Catagory__icontains=request.POST['search'])
        product = product | category
    context = {
        'all_product': product
    }
    return render(request, 'Shop/Addproduct.html', context)


@login_required
def orderproduct(request):
    message = ""
    form = orderform()
    if request.method == "POST":
        form = orderform(request.POST)
        if form.is_valid():
            form.save()
            message = "your order is confirm"
            form = orderform()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Shop/OrderProduct.html', context)


def showDetails(request, product_id):
    searched_product = get_object_or_404(AddProduct, id=product_id)

    context = {
        'search': searched_product,

    }
    return render(request, 'Shop/details.html', context)


def showConfirm(request):
    return render(request, 'Shop/confirm.html')
