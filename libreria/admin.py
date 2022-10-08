from django.contrib import admin
from .models import Mouses
# Register your models here.
admin.site.register(Mouses)

from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('adminuser', 'dev@email.io', 'password')