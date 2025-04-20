from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def user_registration(request):

    user_form = UserCreationForm()

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()

    context = {
        'form' : user_form
    }

    return render(request,'User/registration.html',context)