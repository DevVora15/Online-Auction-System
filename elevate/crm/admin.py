from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Contact
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'birthday']  # Add 'birthday' to list_display
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('birthday','address')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact)
