from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import *

# setting the 'view site' URL for admin panel
admin.site.site_url = "/api"

# registering our custom user model
admin.site.register(CustomUser, UserAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "ceo_name", "inception_date", "address"]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Team)
