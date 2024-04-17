from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.products_sell ,name ="index"),
    path('account',views.account ,name ="account"),
    path('checkCode',views.checkCode ,name ="checkCode"),
    path('customerAdmin',views.customerAdmin,name="customerAdmin"),
    path('totalViews',views.totalViews,name='totalViews'),
    path('removeUser',views.removeUser,name='removeUser')

]