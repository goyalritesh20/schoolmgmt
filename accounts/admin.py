from django.contrib import admin
from accounts import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Subject)
admin.site.register(User)
