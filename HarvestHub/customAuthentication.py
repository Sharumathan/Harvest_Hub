from django.contrib.auth.backends import BaseBackend
from .models import *

class FarmerAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user = Farmer.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Farmer.objects.get(pk=user_id)
        except Farmer.DoesNotExist:
            return None

class FarmerManagerAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user = FarmerManager.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return FarmerManager.objects.get(pk=user_id)
        except FarmerManager.DoesNotExist:
            return None