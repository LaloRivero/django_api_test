''' Companies admin config '''

from django.contrib import admin

# Models
from companies.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display=['id','name','description', 'ticker', 'values']
