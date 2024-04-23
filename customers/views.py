# Create your views here.
import datetime
import random
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .models import CustomUser, Products, graphDetails
from django.contrib import messages
from .forms import SignupForm
from django.db.models import Q

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate

from .models import CustomUser
from .forms import SignupForm

from customers.myFunctions import  myFunctions
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import CustomUser

from django.http import JsonResponse

# Create your views here.

def payment(request):
    return render(request,'customer/payment.html')


def removeUser(request):
    logout(request)
    return redirect('account')
    
def totalViews(request):
    querySet = graphDetails.objects.all()
    dct = {
        'lable':[],
        'data':[]
    }
    for data in querySet:
        dct['lable'].append(data.month),
        dct['data'].append(data.customerCount)

    return JsonResponse(dct)

def login_signup(request):
    return render(request,'customer/login_signup.html')

def products_sell(request):

    if request.method == 'POST':
        sort = request.POST['sort']
        if sort == 'Fruits':
            find_now = Q(category__icontains="Fruits")
            fruits = Products.objects.filter(find_now)
            return render(request,'customer/product_sell.html',{'all_products':fruits}) 
        elif sort == 'VeGEE':
            find_now = Q(category__icontains="Vegetable")
            fruits = Products.objects.filter(find_now)
            return render(request,'customer/product_sell.html',{'all_products':fruits}) 
        elif sort == 'Leaves':
            find_now = Q(category__icontains="Leaf Item")
            fruits = Products.objects.filter(find_now)
            return render(request,'customer/product_sell.html',{'all_products':fruits}) 
        elif sort == 'search_Pro':
            print("Search pro")
            content = request.POST['searchProduct']
            find_now = Q(Q(category__icontains=content)|Q(product_title__icontains=content)|Q(description__icontains=content))
            fruits = Products.objects.filter(find_now)
            return render(request,'customer/product_sell.html',{'all_products':fruits}) 
    all_products = Products.objects.all()
    return render(request,'customer/product_sell.html',{'all_products':all_products}) 
   
def overView(request):
    return render(request,'customer/overView.html',{'total_customer':myFunctions.total_customer(),"customer_growth":myFunctions.customer_growth(),"product_growth":myFunctions.product_growth()})

def adminCustomer(request):
    view_Enabled = None
    if request.method == "POST":
        if request.POST['adminCustomer_button'] == "Remove":
            username = request.POST['username']
            getUser = CustomUser.objects.get(username=username)
            getUser.delete()
            myFunctions.updateCustomerData()

        if request.POST['adminCustomer_button'] == "View":
            username = request.POST['username']
            view_Enabled = CustomUser.objects.get(username=username)
            print(view_Enabled.first_name)

        if request.POST['adminCustomer_button'] == "search":
            search_content = request.POST['searchContent']
            find_now = Q(Q(first_name__icontains=search_content)|Q(last_name__icontains=search_content)|Q(email__icontains=search_content)|Q(username=search_content))
            customers = CustomUser.objects.filter(find_now)
            return render(request,'customer/adminCustomer.html',{'customers':customers,'view_Enabled':view_Enabled})
    customers = CustomUser.objects.all()
    return render(request,'customer/adminCustomer.html',{'customers':customers,'view_Enabled':view_Enabled})
    

def addItems(request):
    updateProduct = None
    all_products = Products.objects.all()
    if request.method == "POST":
        if request.POST['addnow'] == "ADD NOW":
            try:
                category =request.POST['category']
                productImage =request.FILES.get('productImage')
                title =request.POST['title']
                price =request.POST['price']
                date =request.POST['date']
                lifeTime =request.POST['lifeTime']
                description =request.POST['description']
                if Products.objects.filter(product_title=title).exists():
                    messages.info(request,'Product Title Already exist !')
                else:
                    add_product = Products(date_added=date,price=price,category=category,product_title=title,image=productImage,description=description,life_time=lifeTime)
                    add_product.save()
                    if add_product is not None:
                        print("Sucessfully added")
                        messages.info(request,'Sucessfully added')
                    else:
                        print("something wrong")

            except:
                messages.info(request,'Please fill the details correctly')
        elif request.POST['addnow'] == "Delete":
            product = request.POST['product']
            getUser = Products.objects.filter(product_title=product)
            getUser.delete()

        elif request.POST['addnow'] == "Update":
            product = request.POST['product']
            updateProduct = Products.objects.filter(product_title=product).first()
            print(updateProduct.product_title)

        elif request.POST['addnow'] == "UPDATE NOW":
            updateable_product_title = request.POST['updateable']
            category =request.POST['category']
            title =request.POST['title']
            price =request.POST['price']
            date =request.POST['date']
            lifeTime =request.POST['lifeTime']
            image = request.FILES.get('productImage')
            description =request.POST['description']
            from datetime import datetime
            updateProduct = Products.objects.get(product_title=updateable_product_title)

            updateProduct.category = category
            updateProduct.product_title = title
            updateProduct.price = price
            updateProduct.date_added =datetime.strptime("2024-04-21", "%Y-%m-%d").date()
            updateProduct.life_time = lifeTime
            updateProduct.description = description
            if image is not None:
               updateProduct.image = image
            
            updateProduct.save()

        elif request.POST['addnow'] == "+":
            return render(request,'customer/addItems.html',{"all_products":all_products})
    return render(request,'customer/addItems.html',{"all_products":all_products,"updateProduct":updateProduct})

def graphView(request):
    return render(request,'customer/graphView.html')

def account(request):
    if request.method == 'POST':
        submit = request.POST['submit']
        #register
        if submit == 'Sign Up':
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            email = request.POST['email']
            phone_number = request.POST['phoneNo']
            password = request.POST['password1']
            re_password = request.POST['password2']
            username = "RC"+str(phone_number)

            if password == re_password:
                if CustomUser.objects.filter(phone_number = phone_number).exists():
                    messages.info(request,'Phone Number already Exist')
                    return redirect('account')
                else:
                    user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name,email=email,phone_number=phone_number,password=password,username=username)
                    if user is not None:
                        user.save()
                        '''message = f'We are delighted to welcome you to the HarvestHub family. Your decision to join us is greatly appreciated, and we are thrilled to have you as a valued member of our community.\n\nWe are pleased to inform you that you are now a registered customer of our company. This grants you full access to all the features and services available on our website. From this point onwards, you can enjoy seamless navigation and utilize our customer services as needed.\n\nTo begin accessing your account, please utilize the following login credentials:\n\n\n\nUsername: {username}\n\nPassword: {password}\n\n\n\nShould you encounter any queries or require assistance, please do not hesitate to reach out to us. We are here to ensure your experience with HarvestHub is as smooth and rewarding as possible.\n\nOnce again, thank you for choosing HarvestHub. We look forward to serving you and providing you with exceptional service.\n\n\n\n\nWarm regards,\n\nHarvestHub team\nCustomer manager\nHarvestHub'
                        email = EmailMessage(
                        f'Account created',f'Dear {first_name},\n\n{message}'
                        ,settings.EMAIL_HOST_USER,[email]
                            )

                        email.fail_silently = True
                        email.send()'''
                        messages.info(request,'Check your Email for User Name')
                    
            else:
                messages.info(request,'Password Not Match')
                return redirect('account')
            
        #login
        elif(submit == 'Sign In'):

            username = request.POST['username']
            password = request.POST['password']
            user_Devider = request.POST['user_Devider']
            
            if user_Devider == 'User':
                if username == 'sharu' and password == '1234':
                    myFunctions.printName()
                    myFunctions.updateCustomerData()
                    myFunctions.updateProductData()
                    return render(request,'customer/overView.html',{'total_customer':myFunctions.total_customer(),"customer_growth":myFunctions.customer_growth(),"product_growth":myFunctions.product_growth()})
                else:
                    print(username)
                    print(password)
                    user = CustomUser.objects.authenticate(username=username, password=password)
                    if user is not None:
                        print(user.email)
                        login(request,user)
                        all_products = Products.objects.all()
                        return render(request,'customer/product_sell.html',{'all_products':all_products}) 
                    else:
                        messages.info(request,'Login Failed')
                        return render(request,'customer/login_signup.html') 
            elif user_Devider == 'Farmer Manager':
                print("farmer manager")
            elif user_Devider == 'Farmer':
                print("farmer")
        #forgot password
        elif(submit== 'Continue'):
            username = request.POST['username']
            details = CustomUser.objects.getDetails(username=username)
            if details is not None:
                hint = details[0][0:4]
                code = random.randint(111111,999999)
                message = f"\n\nWe hope this message finds you well. We have received your request for a forgot password for your HarvestHub account. As part of our commitment to ensuring the security of your account, we have generated a unique recovery code for you to use. Please find your recovery code below:\n\n\n\nRecovery Code:{code}\n\n\n\nTo reset your password, kindly follow the link provided in our previous correspondence and enter the above recovery code when prompted. Once completed, you will be able to set a new password for your account.\n\nIf you did not initiate this request or have any concerns regarding the security of your account, please contact our support team immediately for further assistance.\n\nThank you for your cooperation and understanding.\n\nBest regards,\n\nHarvet hub team \nCustomer Manager\nHarvestHub"   
                email = EmailMessage(
                        f'Recover Password',f'Dear {details[1]},\n\n{message}'
                        ,settings.EMAIL_HOST_USER,[details[0]]
                            )

                email.fail_silently = True
                email.send()
                 
                return render(request,'customer/enterCode.html',{'hint':hint,'code':code,'username':username})
            else:
                messages.info(request,'Enter correct username')
                return render(request,'customer/login_signup.html') 
            

    else:
        pass

    return redirect('/')

def checkCode(request):
    if request.method == 'POST':
        code = request.POST['code']
        username = request.POST['username']
        usercode = request.POST['userCode']
        print(code)
        if code == usercode :
                details = CustomUser.objects.getDetails(username)
                message = f"\n\nWe are pleased to inform you that your password reset request for your HarvestHub account has been successfully processed. As a result, we are providing you with your updated login credentials to access your account.\n\nUsername: {username}\nPassword: {details[2]}\n\nChanging your password is adviced profile settings \n\nPlease ensure to keep this information secure and confidential to maintain the integrity of your account. We recommend logging in as soon as possible to verify the changes and to continue enjoying the full range of services and features offered by HarvestHub.\n\nShould you encounter any issues or require further assistance, please do not hesitate to reach out to our support team. We are here to help ensure a smooth and seamless experience for all our valued users.\n\nThank you for your attention to this matter, and we look forward to serving you further.\n\nBest regards,\n\nHarvest Hub team\nCustomer Manager\nHarvestHub"
                email = EmailMessage(
                        f'Recover Password',f'Dear {details[1]},\n\n{message}'
                        ,settings.EMAIL_HOST_USER,[details[0]]
                            )

                email.fail_silently = True
                email.send()
    return redirect('/')