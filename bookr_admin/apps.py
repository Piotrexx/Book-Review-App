from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class BookrAdminConfig(AdminConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'bookr_admin'
    default_site = 'bookr_admin.admin.BookrAdmin'