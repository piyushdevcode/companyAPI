from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import *

# setting the 'view site' URL for admin panel
admin.site.site_url = "/api"

# registering our custom user model
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Company)
admin.site.register(Team)
