from django.contrib import messages
from django.shortcuts import render, redirect
from restaurant.forms import Restaurantform
from restaurant.models import Restaurantmodel

# Create your views here.
def restaurant_log_reg(request):
    return render(request, 'restaurant/restaurant_log_res_main.html')


def restaurant_login(request):
    return render(request,"restaurant/restaurant_login.html")


def restaurant_registration(request):
    return render(request,"restaurant/restaurant_registration.html",{"rr":Restaurantform()})


def restaurant_registration_saved(request):
    rr=Restaurantform(request.POST)
    if rr.is_valid():
        db=rr.save(commit=False)
        db.restro_otp=5454
        db.restro_status='pending'
        db.save()
        messages.success(request,"Once the admin approve the Regisration you will receive an Email and a TEXT Message!!!")
        return redirect('restaurant_log_reg')
    else:
        return render(request,"restaurant/restaurant_registration.html",{"rr":rr})


def restaurant_login_saved(request):
    rus=request.POST.get('rl1')
    rpsd=request.POST.get('rl2')
    try:
        Restaurantmodel.objects.get(restro_name=rus,restro_password=rpsd,restro_status='accepted')
        return render(request,"restaurant/dummyyyyyy.html")
    except Restaurantmodel.DoesNotExist:
        messages.error(request,"u dont have permission to login please go and register first ..Already register means wait for the the email conformation ... Thank you!!!!!!!!")
        return redirect('restaurant_login')