from django.contrib import messages
from django.shortcuts import render, redirect
from restaurant.forms import Restaurantform
from swiggy import settings as se
from django.core.mail import send_mail
from restaurant.models import Restaurantmodel
import random

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
           data=rus
           res=Restaurantmodel.objects.get(restro_name=rus)
           return render(request,"restaurant/restaurant_home.html",{"name":data,"dat":res})
    except Restaurantmodel.DoesNotExist:
        message = "invalid user ..please check username and password is register or not!!!"
        return render(request, "restaurant/restaurant_login.html", {"rr": Restaurantform(), "error": message})




def forget_password_page(request):
    return render(request,"restaurant/forget_password_page.html")

otp=0
def reset_password_email(request):
    try:
      rt_un=request.POST.get('fp1')
      rt_em=request.POST.get('fp2')
      print(rt_un,rt_em)
      if request.method=='POST':
         rno=random.randint(10000,99999)
         global otp
         otp=rno
         print(otp)
         Restaurantmodel.objects.filter(restro_name=rt_un,restro_email=rt_em).update(restro_otp=otp)
         subject='password reset conformation'
         message='u r conformation otp is :'+str(otp)
         print(subject,message)
         send_mail(
             subject,
             message,
             se.EMAIL_HOST_USER,
             [rt_em]
         )
         print(send_mail)
         return render(request,"restaurant/password_reset_sent.html")
      else:
          messages.error(request, "invalid email")
          return redirect('forget_password_page')

    except Restaurantmodel.DoesNotExist:
        messages.error(request,"invalid")
        return redirect('forget_password_page')


def otp_validate(request):
    etp=request.POST.get('otp1')
    if request.method=='POST':
        Restaurantmodel.objects.filter(restro_otp=etp)
        return render(request,"restaurant/password_reset_form.html")
    else:
        messages.error(request,"invalid OTP please try again!!!!!!!!!")
        return redirect('reset_password_email')


def reset_password_conformation(request):
    npsd=request.POST.get('npsd1')
    npd=request.POST.get('npsd2')
    if npsd==npd:
        Restaurantmodel.objects.filter(restro_password=npsd).update(restro_password=npd)
        return render(request,"restaurant/password_reset_complete.html")
    else:
        messages.error(request,"u r entred password is different please be check!!!")
        return redirect('otp_validate')