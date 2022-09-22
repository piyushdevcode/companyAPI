from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import *
# Register your models here.
admin.site.site_url = '/api'
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Company)
admin.site.register(Team)
