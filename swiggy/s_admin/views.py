from django.shortcuts import render,redirect
from django.views import View
from s_admin.models import AdminLoginModel,Statemodel,Citymodel,Areamodel,RestaurantType
from restaurant.models import Restaurantmodel
from .forms import Stateform,Cityform,Areaform,RestaurantTypeForm
from django.contrib import messages
# Create your views here.
def Homepage(request):
    return render(request,"common.html")


class admin_login(View):
    def get(self,request):
      return render(request,"s_admin/admin_login.html")
    def post(self,request):
        ad_un=request.POST.get('admin_username')
        ad_psd=request.POST.get('admin_password')
        try:
          AdminLoginModel.objects.get(username=ad_un,password=ad_psd)
          request.session['status']=True
          return redirect('admin_body_page')
        except AdminLoginModel.DoesNotExist:
            messages.error(request,"INVALID PASSWORD !!!!!!!!!!!")
            return redirect('admin_login')

def admin_logout(request):
    request.session['status']=False
    return redirect('admin_login')

def admin_body_page(request):
    return render(request,"s_admin/admin_body_page.html")


class open_state(View):
    def get(self,request):
      return render(request,"s_admin/open_state.html",{"sf":Stateform(),'sdata':Statemodel.objects.all()})
    def post(self,request):
        sf=Stateform(request.POST)
        if sf.is_valid():
            sf.save()
            messages.success(request,"State Added Successfully dude!!!!!!!!!!!!")
            return redirect('open_state')
        else:
            return render(request,"s_admin/open_state.html",{"sf":sf})


def update_state(request):
    sno=request.GET.get('sno')
    sname=request.GET.get('sname')
    d1={'sno':sno,"sname":sname}
    return render(request,"s_admin/open_state.html",{"update_data":d1,'sdata':Statemodel.objects.all()})


def update_state_data(request):
    sno=request.POST.get('s1')
    sname=request.POST.get('s2')
    Statemodel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno=request.GET.get('sno')
    Statemodel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


class open_city(View):
    def get(self,request):
        return render(request,"s_admin/open_city.html",{'cf':Cityform(),"cdata":Citymodel.objects.all()})
    def post(self,request):
        cf=Cityform(request.POST)
        if cf.is_valid():
            cf.save()
            messages.success(request,"City Added Successfully dude!!!!!!!!!")
            return redirect('open_city')
        else:
            return render(request,"s_admin/open_city.html",{"cf":cf})


def delete_city(request):
    cno=request.GET.get('cno')
    Citymodel.objects.filter(city_no=cno).delete()
    return redirect('open_city')


def update_city(request):
    cno=request.GET.get('cno')
    cname=request.GET.get('cname')
    d1={"cno":cno,"cname":cname}
    return render(request,"s_admin/open_city.html",{'update_data':d1,"cdata":Citymodel.objects.all()})


def update_city_data(request):
    cno=request.POST.get('c1')
    cname=request.POST.get('c2')
    Citymodel.objects.filter(city_no=cno).update(city_name=cname)
    return redirect('open_city')


class open_area(View):
    def get(self,request):
        return render(request,"s_admin/open_area.html",{'af':Areaform(),'adata':Areamodel.objects.all()})
    def post(self,request):
        af=Areaform(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request,"Area Added Successfully dude!!!!!!!")
            return redirect('open_area')
        else:
            return render(request,"s_admin/open_city.html",{"af":af})
def update_area(request):
    ano=request.GET.get('ano')
    aname=request.GET.get('aname')
    d1={"ano":ano,"aname":aname}
    return render(request,"s_admin/open_area.html",{"update_data":d1,"adata":Areamodel.objects.all()})

def update_area_data(request):
    ano=request.POST.get('a1')
    aname=request.POST.get('a2')
    Areamodel.objects.filter(area_no=ano).update(area_name=aname)
    return redirect('open_area')

def delete_area(request):
    ano=request.GET.get('ano')
    Areamodel.objects.filter(area_no=ano).delete()
    return redirect('open_area')


class open_type(View):
     def get(self,request):
         return render(request,"s_admin/open_type.html",{'rtf':RestaurantTypeForm(),'rtdata':RestaurantType.objects.all()})
     def post(self,request):
         rtf=RestaurantTypeForm(request.POST)
         if rtf.is_valid():
             rtf.save()
             messages.success(request,"Type Added Successfully dude!!!!!!")
             return redirect('open_type')
         else:
             return render(request,"s_admin/open_type.html",{'rtf':rtf})


def delete_type(request):
    rtno=request.GET.get('rtno')
    RestaurantType.objects.filter(type_no=rtno).delete()
    return redirect('open_type')


def update_type(request):
    rtno=request.GET.get('rtno')
    rtname=request.GET.get('rtname')
    d1={'rtno':rtno,'rtname':rtname}
    return render(request,"s_admin/open_type.html",{'update_data':d1,'rtdata':RestaurantType.objects.all()})


def update_type_data(request):
    tno=request.POST.get('t1')
    tname=request.POST.get('t2')
    RestaurantType.objects.filter(type_no=tno).update(type_name=tname)
    return redirect('open_type')


def restro_menu(request):
    return render(request,"s_admin/restro_menu.html")


def pending_restro(request):
    prest=Restaurantmodel.objects.filter(restro_status='pending')
    return render(request,"s_admin/pending_restro.html",{"data":prest})


def rejected_restro(request):
    rno=request.GET.get('rno')
    Restaurantmodel.objects.filter(restro_id=rno).update(restro_status='rejected')
    return redirect('pending_restro')


def show_rejected_restro(request):
    rs=Restaurantmodel.objects.filter(restro_status='rejected')
    return render(request,"s_admin/show_rejected_restro.html",{"data":rs})


def approved_restro(request):
    rno=request.GET.get('rno')
    Restaurantmodel.objects.filter(restro_id=rno).update(restro_status='accepted')
    return redirect('pending_restro')


def show_accepted_restro(request):
    rs=Restaurantmodel.objects.filter(restro_status='accepted')
    return render(request,"s_admin/show_accepted_restro.html",{"data":rs})