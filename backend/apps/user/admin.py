from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import User

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'id_number',
                'id_type',
                'phone',
                'user_type',
            ),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('id_number', 'id_type', 'phone', 'dob', 'user_type')
        }),
    )

admin.site.register(User, CustomUserAdmin)
