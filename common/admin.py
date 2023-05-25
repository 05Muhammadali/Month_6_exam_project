from django.contrib import admin

from common.models.about_us import AboutUs
from common.models.category import Category
from common.models.contact_us import ContactUs

admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(ContactUs)