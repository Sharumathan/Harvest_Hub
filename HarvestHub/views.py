from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import requests
from .forms import *
from .models import *
from django.contrib import messages
import json
import requests
from django.contrib.auth import authenticate,login,logout
from .customAuthentication import *
import random
from collections import defaultdict
from django.db.models import Q



# Create your views here.
def get_weather(city):
    api_key = '4a4f69a5f1574de4099726e3c9fa2f6c'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Construct the URL
    complete_url = f"{base_url}q={city}&appid={api_key}"

    # Get response from the API
    response = requests.get(complete_url)

    # Parse response
    data = response.json()

    # Extract relevant weather information
    if data["cod"] != "404":
        weather_data = {
            "city": data['name'],
            "temperature": round(data['main']['temp'] - 273.15, 2),  # Temperature in Celsius
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "wind_speed": data['wind']['speed'],
            "wind_direction": data['wind']['deg'] if 'deg' in data['wind'] else None,
        }
        return weather_data
    else:
        return None




def get_city_image(city):
    api_key = 'AIzaSyDQNrN4SiFQIYxPfEEicXQ02vI77q4muOM'
    search_engine_id = '33277f56040b04439'
    search_query = f'{city} city'

    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={search_query}&searchType=image'

    try:
        response = requests.get(url)
        data = response.json()

        # Extract image URL from the response
        if 'items' in data and len(data['items']) > 0:
            image_url = data['items'][0]['link']
            return image_url
        else:
            return 'https://example.com/default_image.jpg'  # Return a default image if no image found
    except Exception as e:
        print(f"Error fetching image: {e}")
        return 'https://example.com/default_image.jpg'  # Return a default image in case of any error



def weather_report(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        
        if request.method == 'POST':
            city = request.POST.get('inputField1')
        
            weather_data = get_weather(city)
            cityimage = get_city_image(city)
            
            response_data = {
            'weather_data': weather_data,
            'city_image': cityimage
            }
            # Return the response as JSON
            return JsonResponse(response_data)
        else:
            current_user = request.user
            farmer = Farmer.objects.filter(username=current_user).first()  
            user_city = farmer.city
            city = user_city  
            
            weather_data = get_weather(city)
            cityimage = get_city_image(city)
            return render(request, 'farmer/weather_report.html', {'weather_data': weather_data, 'cityimage':cityimage })
    else:
        return redirect('login')



def graph_view(request):
    
    sales = Sales.objects.filter(user='mathushan')
    
    return render(request, 'farmer/graph_template.html', {'sales':sales})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:   
        if request.method == 'POST':
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_type = request.POST.get('user_type')
            
            if user_type == 'Farmer':
                user = FarmerAuthBackend().authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user, backend='HarvestHub.customAuthentication.FarmerAuthBackend')
                    return redirect('Graph')
            elif user_type == 'FarmerManager':
                user = FarmerManagerAuthBackend().authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user, backend='HarvestHub.customAuthentication.FarmerManagerAuthBackend')
                    return redirect('manager_dashboard')
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("login")

        return render(request, 'farmer/login.html')



def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect("/")


def register_farmer(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            if Farmer.objects.filter(username=username).exists():
                return render(request, 'farmer/farmer_registration.html', {'alert_message': 'Username already exists.'})
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            city = request.POST.get('city')
            phone = request.POST.get('phone')
            profile_picture = request.FILES.get('file')
            gender = request.POST.get('name')
            farmer = Farmer.objects.create_user(password = password1, username = username, email = email, Image = profile_picture, phone_number = phone, 
                                                city = city, gender = gender)
            farmer.save()
            return redirect('login')
        else:
            return render(request, 'farmer/farmer_registration.html')
    else:
        return redirect('/')
    


def farmer_manager_dashboard(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        return render(request, 'farmer/farmer_manager_dashboard.html')
    else:
        return redirect('login')



def collection(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        catagory=Catagory.objects.filter(status=0)
        return render(request,"farmer/collection.html",{"catagory":catagory})
    else:
        return redirect('login')
      


def collectionsview(request,name):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        if(Catagory.objects.filter(name=name,status=0)):
            products=Product.objects.filter(category__name=name)
            return render(request,"farmer/products.html",{"products":products,"category_name":name})
        else:
            return redirect('farmer/collection')
    else:
        return redirect('login')
    
    
 
def product_details(request,cname,pname):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        if(Catagory.objects.filter(name=cname,status=0)):
            if(Product.objects.filter(name=pname,status=0)):
                products=Product.objects.filter(name=pname,status=0).first()
                return render(request,"farmer/product_details.html",{"products":products})
            else:
                return redirect('collections')
        else:
            return redirect('collections')
    else:
        return redirect('login')
  
  

def favorite_viewpage(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        favorite = Favourite.objects.filter(user=request.user)
        return render(request,"farmer/favorite.html",{"favorite":favorite})
    else:
        return redirect('login')
 
 

def favorite_page(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_farmer:
                data=json.load(request)
                product_id=data['pid']
                product_status=Product.objects.get(id=product_id)
                if product_status:
                    if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'Product Already in Favourite'}, status=200)
                    else:
                        Favourite.objects.create(user=request.user,product_id=product_id)
                        return JsonResponse({'status':'Product Added to Favourite'}, status=200)
                else:
                    return JsonResponse({'status':'Login to Add Favourite'}, status=200)
            else:
                return JsonResponse({'status':'Invalid Access'}, status=200) 
    else:
        return redirect('login')
 
 
 
def remove_favorite(request, fid):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        item=Favourite.objects.get(id = fid)
        item.delete()
        return redirect("favorite_viewpage")
    else:
            return redirect('login')
    
    
 
def cart_page(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        cart=Cart.objects.filter(user=request.user)
        return render(request,"farmer/cart.html",{"cart":cart})
    else:
        return redirect('login')
  
 
 
 
def remove_cart(request,cid):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        cartitem=Cart.objects.get(id=cid)
        cartitem.delete()
        return redirect("cart")
    else:
        return redirect('login')
 
 
def add_to_cart(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_farmer:
                data=json.load(request)
                product_qty=data['product_qty']
                product_id=data['pid']
                product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)
            else:
                return JsonResponse({'status':'Login to Add Cart'}, status=200)
        else:
            return JsonResponse({'status':'Invalid Access'}, status=200)
    else:
        return redirect('login')



def sales_view(request):
    if request.user.is_authenticated and isinstance(request.user, Farmer):
        if request.method == 'POST':
            user = request.user
            name = request.POST.get('name')
            quantity = request.POST.get('quantity')
            
            total = request.POST.get('total')
            numeric_value_str = total.replace(' Rs', '').replace(',', '')
            total = float(numeric_value_str)
            
            sales = Sales(user = user, name = name, quantity = quantity, total_amount = total)
            sales.save()
            sell_product = SalesProductPrice.objects.all()
            return render(request, 'farmer/sales.html', {'message':"Your Request Was Sent Successfully.", 'sell_product':sell_product})
        sell_product = SalesProductPrice.objects.all()
        return render(request, 'farmer/sales.html', {'sell_product':sell_product})
    else:
         return redirect('login')



def sale_product_price_view(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        product_details = SalesProductPrice.objects.all()
        return render(request, 'farmer/sale_product_price.html',{'product_details':product_details})
    else:
        return redirect('login')
  
  
    
def add_sale_product_price_view(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            sell_product = SalesProductPrice(name = name, price = price)
            sell_product.save()
            return redirect('sale_product_price')
    else:
        return redirect('login')
    

def delete_sale_product_price_view(request, id):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        salesproduct=SalesProductPrice.objects.get(id=id)
        salesproduct.delete()
        return redirect("sale_product_price")
    else:
        return redirect("login")
    

def update_sale_product_price_view(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        if request.method == 'POST':
            id = request.POST.get('p_id')
            name = request.POST.get('u_name')
            price = request.POST.get('u_price')
            sell_product = SalesProductPrice(id = id)
            sell_product.name = name
            sell_product.price = price
            sell_product.save()
            return redirect('sale_product_price')
    else:
        return redirect('login')
    
    
    
def show_sales_farmer_request_view(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        if request.method == 'POST':
            search_query = request.POST.get('search_query', None)
            if search_query is not None:
                products = Sales.objects.filter(Q(user__icontains=search_query) | Q(name__icontains=search_query))
                products_list = list(products.values())
                response_data = {'search_result': products_list}
                return JsonResponse(response_data)
            
        sales = Sales.objects.all()
        return render(request, 'farmer/show_sales_farmer_request.html', {'sales':sales})
    else:
        return redirect('login')
    
    

def approve_sales_farmer_request_view(request ,id):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        sales = get_object_or_404(Sales, id=id)
        sales.status = "Approved"
        sales.save()
        return redirect('show_sales_farmer_request')
    else:
        return redirect('login')
    


def delete_sales_farmer_request_view(request ,id):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        sales = get_object_or_404(Sales, id=id)
        sales.delete()
        return redirect('show_sales_farmer_request')
    else:
        return redirect('login')
    
    
    
def show_farmer_detail_view(request):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        farmers = Farmer.objects.values('id', 'username', 'email', 'phone_number', 'city','gender')
        return render(request, 'farmer/show_farmer_detail.html', {'farmers':farmers})
    else:
        return redirect('login')
        
        
        
def delete_farmer_detail(request ,id):
    if request.user.is_authenticated and isinstance(request.user, FarmerManager):
        farmer = get_object_or_404(Farmer, id=id)
        farmer.delete()
        return redirect('show_farmer_detail')
    else:
        return redirect('login')
    
    
    
def test(request):
    return render(request, 'farmer/test.html')



def search(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        search_query = request.POST.get('search_query', None)
        if search_query is not None:
            products = Product.objects.filter(name__icontains=search_query)
            products_list = list(products.values())
            response_data = {'search_result': products_list}
            
            return JsonResponse(response_data)
    
    return render(request, 'farmer/search.html', {'product': products})
"""
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:   
        if request.method == 'POST':
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            # user = FarmerAuthBackend().authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #login(request, user, backend='HarvestHub.customAuthentication.FarmerAuthBackend')
                if isinstance(user, Farmer):
                    return redirect('Graph') 
                elif isinstance(user, FarmerManager):
                    return redirect('manager_dashboard')
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("login")

        return render(request, 'farmer/login.html')
"""