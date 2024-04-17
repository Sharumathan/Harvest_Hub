from . import views
from django.contrib import admin
from django.urls import path 

urlpatterns = [
    path('',views.Home,name="Home"),
    path('addData',views.addData, name="addData"),
    path('View_Details',views.View_Details,name="View_Details"),
    path('Home',views.Home,name="Home"),
    path('updateData/<int:id>',views.updateData, name="updateData"),
    path('deleteData/<int:id>',views.deleteData, name="deleteData"),

    path('payment',views.payment,name="payment"),

    path('paypal-return',views.paypal_return , name='paypal-return'),
    path('paypal_cancel',views.paypal_cancel , name='paypal_cancel'),

]