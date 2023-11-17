from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = CustomUser
    # Fields to filter
    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ('user_name',)
    # Fields to filter
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'is_admin')
    # Fields to be displayed in the user list in the admin panel
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff', 'is_admin')
    # Aditional fields to edit when creating or modifying a user
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 
                                    'groups', 'user_permissions')}),
    )
    # Fields to display when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # Add the wide CSS class to the fields
            'fields': ('email', 'user_name', 'first_name', 'password1', 
                       'password2', 'is_active', 'is_staff', 'is_admin')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
