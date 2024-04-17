from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def Home(request):
    #msg="<h1>Welcome Vithu!</h1>"
    #return HttpResponse(msg)
    #result=os.path.join(BASE_DIR,"Templates")
    #print(result)
    return render(request,"Home.html")

def payment(request):
    return render(request,"payment.html")