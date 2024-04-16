from django.contrib import admin
from .models import *
# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at', 'total_amount', )

    
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(FarmerManager, FarmerManagerAdmin)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesProductPrice)
