from django import forms
from front.models import  Category,Ware,UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="请输入物品分类名称")

    class Meta:

        model = Category
        fields = ('name',)


class WareForm(forms.ModelForm):
    name = forms.CharField(max_length=256, help_text="请输入商品名称")
    price = forms.FloatField(help_text="请输入商品价格")
    picture = forms.ImageField(help_text="请上传商品图片",required=True)

    class Meta:
        model = Ware
        exclude = ('category',)

