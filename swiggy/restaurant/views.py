from django.contrib import messages
from django.shortcuts import render, redirect
from restaurant.forms import Restaurantform
from swiggy import settings as se
from django.core.mail import send_mail
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
        res=Restaurantmodel.objects.get(restro_name=rus,restro_password=rpsd)
        if res.restro_status=='pending':
            messages.error(request,"Hlo  "  +res.restro_name+ " u dont have permission to login please go and register first ..Already register means wait for the the email conformation ... Thank you!!!!!!!!")
            return redirect('restaurant_login')
        elif res.restro_status=="rejected":
            messages.error(request,"Hlo  "+res.restro_name+" u r details are not possible to get permission u r rejected by user!!!!!")
            return redirect('restaurant_login')
        else:
           request.session['status']=True
           return redirect('restaurant_home')
    except Restaurantmodel.DoesNotExist:
        message = "invalid user ..please check username and password is register or not!!!"
        return render(request, "restaurant/restaurant_login.html", {"rr": Restaurantform(), "error": message})

def restaurant_home(request):
    return render(request,"restaurant/restaurant_home.html")


def forget_password_page(request):
    return render(request,"restaurant/forget_password_page.html")


def forget_password_email_page(request):
     eml=request.POST.get('em1')
     try:
         subject='GRPSPK PASSWORD VERIFICATION'
         message='hiii please click the link and follow the flow',
         send_mail(
             subject,
             message,
             se.EMAIL_HOST_USER,
             [eml]
         )
         print(send_mail)
         return render(request, "restaurant/forget_password_email_page.html")
     except:
         messages.error(request,"invalid user")
         return redirect('forget_password_page')

