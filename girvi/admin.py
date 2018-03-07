from django.contrib import admin
from import_export import fields,resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Customer,LoanBill,License,Release
# Register your models here.

class CustomerResource(resources.ModelResource):

    class Meta:
        model=Customer

class LoanBillResource(resources.ModelResource):
    customer=fields.Field(column_name='customer',
                            attribute='customer',
                            widget=ForeignKeyWidget(Customer,'pk'))
    license=fields.Field(column_name='license',
                            attribute='license',
                            widget=ForeignKeyWidget(License,'id'))
    class Meta:
        model=LoanBill
        #import_id_fields = ('id',)
        fields=('id','customer','license','LoanDate','LoanId','ItemType','ItemWeight','ItemDesc','LoanAmount','LoanInt')

class CustomerAdmin(ImportExportModelAdmin):
    list_display=('Name','RelatedAs','RelatedTo','Address','ContactNo','EmailId')
    list_filter=['CreatedOn']
    resource_class=CustomerResource

admin.site.register(Customer,CustomerAdmin)
#class CustomerAdmin(ImportExportModelAdmin):
#    resource_class=CustomerResource


class LoanBillAdmin(ImportExportModelAdmin):
    list_display=('id','LoanDate','LoanId','ItemWeight','ItemType','ItemDesc','LoanAmount','LoanInt')
    list_filter=['LoanDate','ItemType','LoanInt']
    resource_class=LoanBillResource

admin.site.register(LoanBill,LoanBillAdmin)
class ReleaseAdmin(admin.ModelAdmin):
    list_display=('loanbill','ReleaseId','ReleaseDate','InterestPaid')
    list_filter=['ReleaseDate']

admin.site.register(Release,ReleaseAdmin)
class LicenseAdmin(admin.ModelAdmin):
    list_display=('Propreitor','CreatedOn','Lid','Address')
    list_filter=['CreatedOn']

admin.site.register(License,LicenseAdmin)
