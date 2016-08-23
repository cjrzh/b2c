from django.conf.urls import url

from front import views

app_name = 'front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_id>[0-9]+)/add_ware/$',\
        views.add_ware,name='add_ware'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^ware/(?P<ware_id>[0-9]+)/$', views.ware, name='ware'),
    url(r'^administrator/$', views.administrator, name='administrator'),
    url(r'^show_cart/$', views.show_cart, name='show_cart'),
    url(r'^ware/(?P<ware_id>[0-9]+)/add_to_cart$', views.add_to_cart, name='add_to_cart'),
    url(r'^show_cart/delete/(?P<ware_id>[0-9]+)/$', views.delete_from_cart, name='delete_from_cart'),

]