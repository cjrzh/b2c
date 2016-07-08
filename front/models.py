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

    website = models.URLField(blank=True)


    def __str__(self):
        return self.user.username