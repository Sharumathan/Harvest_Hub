from customers.models import CustomUser, graphDetails
from datetime import date

class myFunctions:
     def printName():
          print("hii sharuk welcome admin")

     def updateCustomerData():
          month = date.today().strftime("%B")
          year = date.today().strftime("%Y")
          print(month)
          data = graphDetails.objects.last()
          print(data)
          if data is not None :
               if data.month != month :
                    newData = CustomUser.objects.all().count() - data.customerCount
                    print(newData)
                    added = graphDetails(month=month,customerCount=newData,year=year)
                    added.save()
                    if added is not None:
                         print("addedSucess")
          else :
               newData = CustomUser.objects.all().count()
               print(newData)
               added = graphDetails(month=month,customerCount=newData,year=year)
               if added is not None:
                    print("first time executed")
          
     def total_customer():
          return CustomUser.objects.all().count()