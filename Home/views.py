from django.shortcuts import render

def showhome(request):
    return render(request, 'Home/home.html')

def showabout(request):
    return render(request, 'Home/about.html')