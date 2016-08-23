from django import forms
from front.models import  Category,Ware,UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="请输入物品分类名称")

    class Meta:

        model = Category
        fields = ('name',)


class WareForm(forms.ModelForm):
    name = forms.CharField(max_length=256, help_text="请输入专辑名称")
    price = forms.FloatField(help_text="请输入专辑价格")
    author = forms.CharField(max_length=128,help_text="请输入专辑作者")
    company = forms.CharField(max_length=128,help_text="请输入发行公司")
    picture = forms.ImageField(help_text="请上传专辑图片",required=True)

    class Meta:
        model = Ware
        exclude = ('category',)

class UserProfileForm(forms.ModelForm):
    realname=forms.CharField(max_length=256, help_text="请输入真实姓名",
                             required=True)
    addr=forms.CharField(max_length=256, help_text="请输入收货地址",required=True)
    class Meta:
        model=UserProfile
        exclude=("balance","user",)