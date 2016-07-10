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

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    addr = models.CharField(max_length=256,blank=True)
    balance = models.FloatField(default=0)
    website = models.URLField(blank=True)


    def __str__(self):
        return self.user.username

class Order(models.Model):
    user=models.ForeignKey(User)
    date=models.DateField()
    def __str__(self):
        return self.id

class OrderItems(models.Model):
    order=models.ForeignKey(Order)
    ware=models.ForeignKey(Ware)
    def __str__(self):
        return self.id

class ShopCart(models.Model):
    user=models.ForeignKey(User)
    #date=models.DateField()
    def __str__(self):
        return self.id

class ShopCartItems(models.Model):
    shopCart=models.ForeignKey(ShopCart)
    ware=models.ForeignKey(Ware)
    def __str__(self):
        return self.id