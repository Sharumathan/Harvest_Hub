from django.http import HttpResponse
from .models import Billing_Address
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid

# Create your views here.

from pathlib import Path
import os

#BASE_DIR = Path(__file__).resolve().parent.parent

def Home(request):
    #msg="<h1>Welcome Vithu!</h1>"
    #return HttpResponse(msg)
    #result=os.path.join(BASE_DIR,"Templates")
    #print(result)
    mydata=Billing_Address.objects.all()
    if(mydata!=''):
        return render(request,'Home.html',{'Billing_Address':mydata})
    else:
        return render(request,"Home.html")


def addData(request):                  #127.0.0.1:8000/addData
    if request.method == 'POST':
        firstname=request.POST['firstname']
        email=request.POST['email']
        address=request.POST['address']
        state=request.POST['state']
        zip=request.POST['zip']   

        print(zip)

        obj=Billing_Address()
        obj.Name=firstname
        obj.Email=email
        obj.Address=address
        obj.State=state
        obj.Zip=zip
        obj.save()

        mydata=Billing_Address.objects.all()
        return redirect('Home')

def View_Details(request):
    mydata=Billing_Address.objects.all()
    return render(request,"View_Details.html",{'Billing_Address':mydata})

def updateData(request,id):               #127.0.0.1:8000/updateData
    mydata = Billing_Address.objects.get(id=id)
    if request.method == 'POST':
        firstname=request.POST.get['firstname']
        email=request.POST.get['email']
        address=request.POST.get['address']
        state=request.POST.get['state']
        zip=request.POST.get['zip']

        mydata.Name=firstname
        mydata.Email=email
        mydata.Address=address
        mydata.State=state
        mydata.Zip=zip
        mydata.save()

        return redirect('View_Details')
    
    return render(request,"update.html",{'data':mydata})

def deleteData(request,id):      #127.0.0.1:8000/deleteData
    mydata = Billing_Address.objects.get(id=id)
    mydata.delete()
    return redirect('View_Details')


def payment(request):
    host = request.get_host()

    # What you want the button to do.
    paypal_dict = {
        'business': settings.PAYPAL_RECIEVER_EMAIL,
        'amount': "10000000.00",
        'item_name': "Product 2",
        'invoice': str(uuid.uuid4()),
        'currency_code': "USD",

        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_return': f'http://{host}{reverse("paypal_cancel")}',
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

def paypal_return(request):
    messages.success(request,'You are successfully made a payment!')
    return redirect('payment')

def paypal_cancel(request):
    messages.error(request,'You are payment is Cancelled!')
    return redirect('payment')
