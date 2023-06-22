from django.shortcuts import render,redirect
from Backend.models import admindb, categorydb, Productdb, Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def indexpage(request):
    return render(request,'home.html')

def AddAdmin(request):
    return render(request,'Addadmin.html')

def saveadmin(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('mobile')
        u = request.POST.get('username')
        p = request.POST.get('password')
        im = request.FILES['img']
        obj = admindb(Name=n,Email=e,Contact=c,User=u,Pass=p,Image=im)
        obj.save()
        return redirect(AddAdmin)

def displayadmin(request):
    data = admindb.objects.all()
    return render(request,'AdminDisplay.html',{'data':data})

def edit(request,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request, 'Edit.html', {'data':data})

def update(request,dataid):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('mobile')
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=n,Email=e,Contact=c,User=u,Pass=p,Image=file)
        return redirect(displayadmin)

def delete(request,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)

def AddCategory(request):
    return render(request,'Addcategory.html')

def savecategory(request):
    if request.method=="POST":
        n = request.POST.get('name')
        d = request.POST.get('desc')
        image = request.FILES['img']
        obj = categorydb(Name=n,Description=d,Image=image)
        obj.save()
        return redirect(AddCategory)

def DisplayCategory(request):
    data=categorydb.objects.all()
    return render(request,'DisplayCat.html',{'data':data})

def Editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,'EditCat.html',{'data':data})

def updatecategory(request,dataid):
    if request.method=="POST":
        n = request.POST.get('name')
        d = request.POST.get('desc')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=n,Description=d,Image=file)
        return redirect (DisplayCategory)

def Deletecategory(request,dataid):
    data= categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCategory)

def AddProducts(request):
    data = categorydb.objects.all()
    return render(request,'Products.html',{'data':data})

def Saveproducts(request):
    if request.method=="POST":
        c = request.POST.get('category')
        n = request.POST.get('name')
        p = request.POST.get('price')
        q = request.POST.get('qty')
        d = request.POST.get('desc')
        im = request.FILES['img']
        obj = Productdb(Category=c,Name=n,Price=p,Quantity=q,Description=d,Image=im)
        obj.save()
        return redirect(AddProducts)

def DisplayPro(request):
    data = Productdb.objects.all()
    return render(request,'DisplayProducts.html',{'data':data})

def EditProduct(request,dataid):
    data = Productdb.objects.get(id=dataid)
    # da = categorydb.objects.all()
    print(data)
    return render(request, 'EditPro.html', {'data': data})

def Updateproduct(request,dataid):
    if request.method=="POST":
        c = request.POST.get('category')
        n = request.POST.get('name')
        p = request.POST.get('price')
        q = request.POST.get('qty')
        d = request.POST.get('desc')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
        Productdb.objects.filter(id=dataid).update(Category=c,Name=n,Price=p,Quantity=q,Description=d,Image=file)
        return redirect (DisplayPro)

def DeleteProduct(request,dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayPro)

def loginpage(request):
    return render(request,'login.html')

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def Msgdisplay(request):
    data = Contactdb.objects.all()
    return render(request,'Contact_Msg.html',{'data':data})

def DeleteMsg(request,dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Msgdisplay)


