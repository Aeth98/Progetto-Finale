from django.shortcuts import render
from .forms import Register
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Item, Profile
import redis
def registerpage(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account successfully created.')
            return redirect('loginpage')
    else:
        form = Register()
    return render(request, 'app/registerpage.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'app/loginpage.html', {})

def homepage(request):
    return render(request, 'app/homepage.html', {})

def item_list(request):
    items = Item.objects.filter()
    return render(request, 'app/itemlist.html', {'items': items})

def history(request):
    #user = request.user
    #user_profile = Profile.objects.get(user=user)
    #user_bets = user_profile.bets_list
    return render(request, 'app/history.html', {})

def item_detail(request, pk):
    items = Item.objects.filter()
    item = get_object_or_404(items, pk=pk)
    return render(request, 'app/itemdetail.html', {'item': item})