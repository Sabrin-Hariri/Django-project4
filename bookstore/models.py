import email
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    name=models.CharField(max_length=190 , null=True) 
    email=models.CharField(max_length=190 , null=True) 
    phone=models.CharField(max_length=190 , null=True) 
    avatar = models.ImageField(blank=True, null=True, default="preson.png")
    age=models.CharField(max_length=190 , null=True) 
    date_created=models.DateTimeField(auto_now_add=True , null=True) 

    def __str__(self):
        return self.name 

######################### tag before the book class . one to many 



class Tag(models.Model):
    name = models.CharField(max_length=190, null=True)

    def __str__(self):
       return self.name

#########################3
class Book(models.Model):
    CATEGORY = (
        ('Classics','Classics'),
        ('Comic Book','Comic Book'),
        ('Fantasy','Fantasy'),
        ('spiritual','spiritual'),
        ('علوم روحية','علوم روحية'),
        (' out mind','out mind')
        
    )
    name = models.CharField(max_length=190, null=True)
    author = models.CharField(max_length=190, null=True)
    price = models.FloatField( null=True)
    image = models.ImageField(blank=True, null=True ,default="book2.png")
    file=models.FileField(blank=True, null=True)
    category = models.CharField(max_length=190, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
         return self.name

#############################

class Order(models.Model):
    STATUS= (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('in progress','in progress'),
        ('out of order','out of order')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status =  models.CharField(max_length=200, null=True,choices=STATUS)



