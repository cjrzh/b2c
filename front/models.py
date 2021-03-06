from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Ware(models.Model):
    #一对多关系使用ForeignKey,表示1个分类下有多个物品
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    price = models.FloatField(max_length=128)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    author = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    realname=models.CharField(max_length=128,blank=True)
    addr = models.CharField(max_length=256,blank=True)
    balance = models.FloatField(default=0)


    def __str__(self):
        return self.user.username

class Order(models.Model):
    user=models.ForeignKey(User)
    date=models.DateTimeField("order summit time")
    price=models.FloatField()
    def __str__(self):
        return self.id

class OrderItems(models.Model):
    order=models.ForeignKey(Order)
    ware=models.ForeignKey(Ware)
    def __str__(self):
        return self.id

class ShopCart(models.Model):
    user=models.OneToOneField(User)
    #date=models.DateField()
    def __str__(self):
        return self.id

class ShopCartItems(models.Model):
    shopCart=models.ForeignKey(ShopCart)
    ware = models.ForeignKey(Ware)
    def __str__(self):
        return self.id