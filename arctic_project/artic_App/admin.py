from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(products)
admin.site.register(Cart)
admin.site.register(productnews)
admin.site.register(shopowner)
admin.site.register(Comment)
admin.site.register(CompanyLogo)
admin.site.register(UserQuestios)
admin.site.register(BillingAddress)

