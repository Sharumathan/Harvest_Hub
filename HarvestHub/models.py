from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
import os
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


def create_image_name(instance, filename):
    now_time = timezone.now().strftime("%Y%m%d%H%M%S")
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"{now_time}_{base_filename}{file_extension}"
    return os.path.join(new_filename)

                
class Farmer(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='farmer_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='farmer_permissions'
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    Image = models.ImageField(upload_to=create_image_name, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=1, null=False, blank=False)
    is_farmer = models.BooleanField(default=True)

        
    class Meta:
        verbose_name_plural = 'Farmer'
        

class FarmerAdmin(UserAdmin):
    model = Farmer
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'city', 'gender', 'Image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_farmer')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_farmer')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')


class FarmerManager(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='farmerManager_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='farmerManager_permissions'
    )
    
    is_farmer_manager = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Farmer Manager'

    
class FarmerManagerAdmin(UserAdmin):
    model = FarmerManager
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions', 'is_farmer_manager')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_farmer_manager')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')

   
class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=create_image_name,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=create_image_name,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def total_cost(self):
        return self.product_qty * self.product.price
 
 
class Favourite(models.Model):
	user = models.ForeignKey(Farmer,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
 
 
class Sales(models.Model):
    user = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    quantity = models.FloatField(null=False,blank=False)
    total_amount = models.FloatField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=False, blank=False, default='Process')
    
    
class SalesProductPrice(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    created_at = models.DateField(default=timezone.now)