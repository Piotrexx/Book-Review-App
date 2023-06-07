from django.contrib import admin
from django.contrib.auth.admin import User
from django.contrib.admin.apps import AdminConfig
# Register your models here.

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr admin page"


admin_site = BookrAdmin(name="bookr_admin")
admin_site.register(User)