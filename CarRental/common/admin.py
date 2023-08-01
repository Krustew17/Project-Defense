from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth
from django.utils.html import format_html
from .models import ProfileUser, ContactUsModel

User = get_user_model()


# App User Admin
@admin.register(User)
class AppUserAdmin(auth.UserAdmin):
    list_display = ['username', 'last_login', 'is_staff', 'is_superuser']
    list_filter = ['last_login', 'username']
    ordering = ['pk']
    fieldsets = (
        ('Credentials', {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_per_page = 10
    readonly_fields = ['date_joined', 'last_login']
    search_fields = ['username']


# Profile User Admin
@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'age']
    ordering = ['user']
    list_filter = ['user']
    fieldsets = (
        ('User Information',
         {'fields': ('profile_image', 'first_name', 'last_name', 'age', 'country', 'city', 'phone_number')}),
    )

    list_per_page = 10


# Contact Us Admin
@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'created_at', 'email', 'Message', 'Status', '_']
    ordering = ['created_at', 'admin_message']
    list_filter = ['created_at', 'admin_message', 'status']
    fieldsets = (
        ('Details', {'fields': ('admin_message', 'status', 'name', 'topic', 'created_at', 'email', 'message',)}),
    )
    readonly_fields = ['name', 'topic', 'created_at', 'message', 'email']
    list_per_page = 10

    def Message(self, obj):
        if obj.admin_message == 'Read':
            color = '#6096e0'
        else:
            color = '#e84f4f'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.admin_message))

    Message.allow_tags = True

    def _(self, obj):
        if obj.status == 'Solved':
            return True
        elif obj.status == 'Pending':
            return None
        else:
            return False

    _.boolean = True

    def Status(self, obj):
        if obj.status == 'Solved':
            color = '#28a745'
        elif obj.status == 'Pending':
            color = 'orange'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status))

    Status.allow_tags = True
