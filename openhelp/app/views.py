
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import Departments,Employee,Register,Login

from django.contrib.auth import authenticate,login,logout
from .models import Loginuser,User,Seller,Products


def index(request):
    return render(request, 'homepage\index.html')

def RegisterUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        email=request.POST['email']
        usercontactnumber=request.POST['usercontactnumber']
        data=Loginuser.objects.create_user(username=username,password=password,email=email,usertype='user')
        data.save()
        userdata=User.objects.create(loginid=data,usercontactnumber=usercontactnumber)
        userdata.save()
        return HttpResponse("userdata is updated")
    else:
        return render(request,'user/userregistration.html')
    

def RegisterSeller(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        email=request.POST['email']
        sellercontactnumber=request.POST['sellercontactnumber']
        sellername=request.POST['sellername']
        selleraddress=request.POST['selleraddress']
        sellercertificate=request.FILES['sellercertificate']
        data=Loginuser.objects.create_user(username=username,password=password,email=email,usertype='seller')
        data.save()
        sellerdata=Seller.objects.create(loginid=data,sellercontactnumber=sellercontactnumber,sellername=sellername,selleraddress=selleraddress,sellercertificate=sellercertificate)
        sellerdata.save()
        return HttpResponse("Sellerdata is updated")
    else:
        return render(request,'user/sellerregistration.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        data = authenticate(request,username=username,password=password)
        print (data)
        if data is not None:
            login(request,data)
            if data.usertype=='user':
                return redirect(userhome)
            elif data.usertype=='seller':
                
                return redirect(sellerhome)
            
            #return HttpResponse('user loggedin')
        else:
            return HttpResponse('user not found')
    else:
        return render(request,'user/login.html')  

def userhome(request):
    return render(request, 'user/index.html')


    
def emplogoutnew(request):
    logout(request)
    return redirect(emploginnew)

#-----seller-------------
def sellerhome(request):
    return render (request,'seller/index.html')   

def addproduct(request):
    logindata=Loginuser.objects.get(id=request.user.id)
    sellerId=Seller.objects.get(loginid=logindata)
    if request.method == 'POST':
        productname=request.POST['productname']
        price=request.POST['price']
        quantity=request.POST['quantity']
        productdetails=request.POST['productdetails']
        images=request.FILES['images']
        data=Products.objects.create(productname=productname,price=price,quantity=quantity,productdetails=productdetails,images=images,sellerId=sellerId)
        data.save()
        return HttpResponse("product details updated")
    else:
        return render (request,'seller/addproduct.html')
    
def ProductsList(request):
    data=Products.objects.all()
    return render(request,'seller/productlist.html',{'data':data})
        
