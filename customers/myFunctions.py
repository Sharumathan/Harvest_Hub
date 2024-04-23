from customers.models import CustomUser, Products, graphDetails
from datetime import date
import datetime
from django.db.models import Sum

import calendar
class myFunctions:
     def printName():
          print("hii sharuk welcome admin")
     
     def updateCustomerData():
          current_date = datetime.datetime.now() 
          month = current_date.month
          month = date.today().strftime("%B")
          year = date.today().strftime("%Y")
          data = graphDetails.objects.last()
          print(data)
          if data is not None :
               if str(data.month) == str(month) and int(data.year) == int(year):
                    newData = CustomUser.objects.filter(joined_date__month = current_date.month).count()
                    data.customerCount=newData
                    data.save()
                    print("updated")
               elif str(data.month) != str(month) or int(data.year) != int(year):
                    newData = CustomUser.objects.filter(joined_date__month = current_date.month).count()
                    print(newData)
                    added = graphDetails(month=month,customerCount=newData,year=year)
                    if added is not None:
                         print("addedSucess")
                         added.save()
          else :
               newData = CustomUser.objects.filter(joined_date__month = current_date.month).count()
               if newData is None:
                    added = graphDetails(month=month,customerCount=0,year=year)
                    if added is not None:
                         print("first time executed")
                         added.save()
               else:
                    print(newData)
                    added = graphDetails(month=month,customerCount=newData,year=year)
                    if added is not None:
                         print("first time executed")
                         added.save()

     def updateProductData():
          current_date = datetime.datetime.now() 
          month = current_date.month
          month = date.today().strftime("%B")
          year = date.today().strftime("%Y")
          data = graphDetails.objects.last()
          print(data)
          if data is not None :
               if str(data.month) == str(month) and int(data.year) == int(year):
                    newData = Products.objects.filter(date_posted__month = current_date.month).count()
                    data.productCount=newData
                    data.save()
                    print("updated")
               elif str(data.month) != str(month) or int(data.year) != int(year):
                    newData = Products.objects.filter(date_posted__month = current_date.month).count()
                    print(newData)
                    added = graphDetails(month=month,productCount=newData,year=year)
                    if added is not None:
                         print("addedSucess")
                         added.save()
          else :
               newData = Products.objects.filter(date_posted__month = current_date.month).count()
               if newData is None:
                    added = graphDetails(month=month,productCount=0,year=year)
                    if added is not None:
                         print("first time executed")
                         added.save()
               else:
                    print(newData)
                    added = graphDetails(month=month,productCount=newData,year=year)
                    if added is not None:
                         print("first time executed")
                         added.save()
          
     def total_customer():
          return CustomUser.objects.all().count()
     
     def customer_growth():
          current_date = datetime.datetime.now()
          total_customer = graphDetails.objects.aggregate(sum_of_column=Sum('customerCount'))['sum_of_column']
          
          if total_customer is not None :
               total_sum = total_customer-CustomUser.objects.filter(joined_date__month = current_date.month).count()
               if total_sum == 0:
                    return "100"
               data =(graphDetails.objects.last().customerCount/total_sum)*100
               return format(data, '.1f')
          else:
               return format(0, '.1f')
          
     def product_growth():
          current_date = datetime.datetime.now()
          total_product = graphDetails.objects.aggregate(sum_of_column=Sum('productCount'))['sum_of_column']
          if total_product is not None :
               total_sum = total_product-Products.objects.filter(date_posted__month = current_date.month).count()
               if total_sum == 0:
                    return "100"
               data =(graphDetails.objects.last().productCount/total_sum)*100
               return format(data, '.1f')
          else:
               return format(0, '.1f')