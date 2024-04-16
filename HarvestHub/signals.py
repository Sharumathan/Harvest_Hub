from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import *
from django.conf import settings
import os

@receiver(pre_delete, sender=Farmer)
def delete_Farmer_images(sender, instance, **kwargs):
    # Delete the image file from the storage
    image_path = os.path.join(settings.MEDIA_ROOT, str(instance.Image))
    
    if os.path.exists(image_path):
        os.remove(image_path)