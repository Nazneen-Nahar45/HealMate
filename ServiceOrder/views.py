from django.shortcuts import render
from .form import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def ConfirmOrder(request):
    message = ""
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Successful !"
            form = OrderForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'ServiceOrder/serviceorder.html', context)