from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from front.forms import CategoryForm, WareForm,UserProfileForm
from front.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

def index(request):
    template_name = 'front/index.html'
    #categories = Category.objects.order_by('id')[:5]
    wares = Ware.objects.order_by('id')[:20]
    #print(wares.__getitem__(0))
    context={}
    #context['categories']=categories
    context['wares'] = wares
    response = render(request,template_name=template_name,context=context)

    return response

@staff_member_required
def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return administrator(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, 'front/add_category.html', {'form': form})

def category(request,category_id):
    context={}
    try:
        category=Category.objects.get(id=category_id)
        context['category_name']=category.name
        wares=Ware.objects.filter(category=category)
        context['wares']=wares
        context['category']=category

    except Category.DoesNotExist:
        print("分类不存在")
    return render(request,'front/category.html',context)

@staff_member_required
def add_ware(request,category_id):
    try:
        cat = Category.objects.get(id=category_id)
        print(cat.name)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = WareForm(request.POST,request.FILES)
        if form.is_valid():
            if cat:
                ware = form.save(commit=False)
                ware.category = cat
                ware.save()
                # probably better to use a redirect here.
                return HttpResponseRedirect("/front/category/"+category_id)
        else:
            print(form.errors)
    else:
        form = WareForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'front/add_ware.html', context_dict)

def about(request):
    return render(request,'front/about.html')

@staff_member_required
def administrator(request):
    return render(request,'front/administrator.html')

def ware(request,ware_id):
    context={}
    try:
        ware=Ware.objects.get(id=ware_id)
        context['ware_name']=ware.name
        context['ware']=ware

    except Ware.DoesNotExist:
        print("商品不存在")
    return render(request,'front/ware.html',context)

@login_required
def show_cart(request):
    user=request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    items=ShopCartItems.objects.filter(shopCart=shopcart)
    price=0.0
    num=0
    for item in items:
        num+=1
        price+=item.ware.price
    context={}
    context['items']=items
    context['num']=num
    context['price']='%0.2f'%price
    return render(request,'front/show_cart.html',context)

@login_required
def add_to_cart(request,ware_id):
    user=request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    #items=ShopCartItems.objects.filter(shopCart=shopcart)
    ware=Ware.objects.get(id=ware_id)
    ShopCartItems.objects.get_or_create(shopCart=shopcart,ware=ware)
    return HttpResponseRedirect('/front/show_cart')

@login_required
def delete_from_cart(request,ware_id):
    user=request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    ware=Ware.objects.get(id=ware_id)
    shopcartItem=ShopCartItems.objects.filter(ware=ware).first().delete()

    return HttpResponseRedirect('/front/show_cart')

@login_required
def get_order_info(request):
    user=request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    items=ShopCartItems.objects.filter(shopCart=shopcart)
    price=0.0
    num=0
    for item in items:
        num+=1
        price+=item.ware.price
    userprofile= UserProfile.objects.filter(user=user).first()


    context={}
    #print(userprofile)
    context['userprofile']=userprofile
    context['items']=items
    context['num']=num
    context['price']='%0.2f'%price

    return render(request,'front/get_order_info.html',context)

@login_required
def add_userprofile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('/front/get_order_info')
        else:
            print(form.errors)
    else:
        form = UserProfileForm()

    return render(request, 'front/add_userprofile.html', {'form': form})

@login_required
def update_userprofile(request):
    userfile=UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)


            userfile.realname=profile.realname
            userfile.addr=profile.addr
            userfile.save()

            return HttpResponseRedirect('/front/get_order_info')
        else:
            print(form.errors)
    else:
        init={'realname':userfile.realname,'addr':userfile.addr}
        form = UserProfileForm(initial=init)

    return render(request, 'front/update_userprofile.html', {'form': form})

@login_required
def clear_cart(request):
    user=request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    ShopCartItems.objects.filter(shopCart=shopcart).delete()

@login_required
def submit_order(request):
    user = request.user
    shopcart = ShopCart.objects.get_or_create(user=user)[0]
    items = ShopCartItems.objects.filter(shopCart=shopcart)
    order=Order(user=user,date=timezone.now())
    order.save()
    for item in items:
        #print(item.ware.name)
        OrderItems.objects.get_or_create(order=order, ware=item.ware)
    clear_cart(request)
    return render(request, 'front/submit_order.html')