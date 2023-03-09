from django.contrib import messages
from django.shortcuts import render, redirect
from Backend.models import categorydb, Productdb, Contactdb
from Frontend.models import CustomerDetails
import django.contrib.messages

def homepage(request):
    data = categorydb.objects.all()
    da = Productdb.objects.all()
    return render(request,'HomePage.html',{'data':data, 'da':da})

def aboutus(request):
    data = categorydb.objects.all()
    return render(request,'About.html',{'data':data})

def contactus(request):
    data = categorydb.objects.all()
    return render(request,'Contact.html',{'data':data})

def blog(request):
    data = categorydb.objects.all()
    return render(request,'Blog.html',{'data':data})

def disprodfrmcat(request,itemcatg):
    data = categorydb.objects.all()
    print("==itemcatg==",itemcatg)
    catg = itemcatg.upper()

    products = Productdb.objects.filter(Category = itemcatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data
    }

    return render(request,"ProdfrmCat.html",context)

def ProdSingle(request,dataid):
    data = categorydb.objects.all()
    item = Productdb.objects.filter(id = dataid)
    return render(request,"ProductSingle.html",{'data':data,'item':item})

def Reglogin(request):
    data = categorydb.objects.all()
    da = Productdb.objects.all()
    return render(request,"login_reg.html",{'data':data, 'da':da})

def Savecustomer(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('password')
        confp = request.POST.get('confpassword')
        obj = CustomerDetails(Username=n,Email=e,Password=p,Confirmpassword=confp)
        obj.save()
        messages.success(request,"Registration Successful")
        return redirect(Reglogin)

def Customerlogin(request):
    if request.method=='POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if CustomerDetails.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            messages.success(request, "Login Successful")

            return redirect(homepage)
        else:
            messages.error(request,"Invalid User")
            return render(request,"login_reg.html")

def Customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)

def ContactMsg(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('sub')
        m = request.POST.get('msg')
        obj = Contactdb(Name=n,Email=e,Subject=s,Message=m)
        obj.save()
        return redirect(contactus)
# Create your views here.
