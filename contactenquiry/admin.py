from django.contrib import admin
from contactenquiry.models import contactEnquiry


class contactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','project')

admin.site.register(contactEnquiry,contactEnquiryAdmin)

# Register your models here.
