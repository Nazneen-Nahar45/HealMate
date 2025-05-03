from django.shortcuts import render
from .models import customer
from .form import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def showCustomer(request):
    client = customer.objects.all()

    context = {
        'all_client': client

    }
    return render(request, 'Client/showClient.html',context)





def customerRegistration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()



    context = {
        'form': form
    }

    return render(request, 'Client/registration.html', context)

@login_required
def CustomerProfile(request):
    message=""
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        message = "Invalid information ☹"

        if form.is_valid():
            profile = form.save(commit=False)
            message = "Successfully done 😃"
            profile.user = request.user
            profile.save()
            form = CustomerForm()
    context = {
        'form': form,
        'message' : message
    }

    return render(request, 'Client/profile.html', context)


