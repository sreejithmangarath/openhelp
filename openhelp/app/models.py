from django.db import models

# Create your models here.



from django.contrib.auth.models import AbstractUser





class Loginuser(AbstractUser):
    statuschoices=(('APPROVE','APPROVE'),('REJECT','REJECT'))
    status=models.CharField(choices=statuschoices,max_length=20,default='PENDING',null=True,blank=True)
    usertype=models.CharField(max_length=100)

class Seller(models.Model):
    loginid=models.ForeignKey(Loginuser,on_delete=models.CASCADE)
    sellername=models.CharField(max_length=200)
    selleraddress=models.CharField(max_length=200)
    sellercertificate=models.FileField()
    selleremail=models.CharField(max_length=200)
    sellercontactnumber=models.IntegerField()
class User(models.Model):
    loginid=models.ForeignKey(Loginuser,on_delete=models.CASCADE)
    username=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    usercontactnumber=models.IntegerField()

class Products(models.Model):
    productname=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    sellerId=models.ForeignKey(Seller,on_delete=models.CASCADE)
    images=models.FileField()
    productdetails=models.CharField(max_length=566)

class Bookings(models.Model):
    bookingstatus=models.CharField(max_length=100)
    bookingdate=models.DateField(auto_now_add=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    productid=models.ForeignKey(Products,on_delete=models.CASCADE)

    



        


