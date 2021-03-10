from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "fees",)
    filter_horizontal = ('teachers',)
    raw_id_fields = ('user',)

@admin.register(models.Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user",    "salary",)
    filter_horizontal = ('subjects',)
    raw_id_fields = ('user',)

admin.site.register(models.Subject)

