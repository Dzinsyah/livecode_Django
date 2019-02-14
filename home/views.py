from django.shortcuts import render, redirect
from .models import Home
from .form import Home_form



def home(request):
    add_post = Home.objects.all()
    return render(request, 'home/home.html',{'isihome':add_post})

def input_home(request):
    if(request.method == 'POST'):
        form = Home_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = Home_form()
    return render(request, 'home/input_home.html', {'form':form})

def post_detail(request, post_id):
    post = Home.objects.get(pk=post_id)
    return render (request, 'home/post_detail.html', {'post':post})  
# Create your views here.
