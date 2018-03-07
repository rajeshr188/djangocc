from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from . import views
from .models import LoanBill
from django_filters.views import FilterView
from . filters import CustomerFilter
from . views import LoanBillYearArchiveView,LoanBillMonthArchiveView
app_name='girvi'
urlpatterns = [
    path('',views.index,name='index'),
    #listviews from models
    #path('customer/',views.CustomerListView.as_view(),name='customer-list'),
    path('customer/',FilterView.as_view(paginate_by= 100,filterset_class=CustomerFilter,template_name='girvi/customer_list.html'),name='customer-list'),
    path('loanbill/',views.LoanBillListView.as_view(),name='loanbill-list'),
    path('license/',views.LicenseListView.as_view(),name='license-list'),
    path('release/',views.ReleaseListView.as_view(),name='release-list'),
    path('ledger/',views.LedgerListView.as_view(),name='ledger-list'),
    path('archive/',ArchiveIndexView.as_view(model=LoanBill,date_field='LoanDate'),name="loanbill-archive"),
    path('archive/<int:year>/',LoanBillYearArchiveView.as_view(),name='loanbill-archive-year'),
    path('archive/<int:year>/<int:month>',LoanBillMonthArchiveView.as_view(month_format='%m'),name='loanbill-archive-month'),
    #details views for models
    path('customer/<int:pk>',views.CustomerDetailView.as_view(),name='customer-detail'),
    path('loanbill/<int:pk>',views.LoanBillDetailView.as_view(),name='loanbill-detail'),
    #path('print/',views.LoanBillDetailPDFView.as_view(),name='billprint'),
    path('loanbill/<int:pk>/print',views.PDFLoanBillDetailView.as_view(),name='loanbill-detail-pdf'),
    path('release/<int:pk>',views.ReleaseDetailView.as_view(),name='release-detail'),
    path('license/<int:pk>',views.LicenseDetailView.as_view(),name='license-detail'),

    #CreateViews for models
    path('customer/create',views.CustomerCreate.as_view(),name='customer-create'),
    path('loanbill/create',views.LoanBillCreate.as_view(),name='loanbill-create'),
    path('loanbill/create/<int:pk>',views.LoanBillCreate.as_view(),name='loanbill-create'),
    path('release/create',views.ReleaseCreate.as_view(),name='release-create'),
    path('release/create/<int:pk>',views.ReleaseCreate.as_view(),name='release-create'),
    path('license/create',views.LicenseCreate.as_view(),name='license-create'),

    path('customer/<int:pk>/update',views.CustomerUpdate.as_view(),name='customer-update'),
    path('loanbill/<int:pk>/update',views.LoanBillUpdate.as_view(),name='loanbill-update'),
    path('release/<int:pk>/update',views.ReleaseUpdate.as_view(),name='release-update'),
    path('license/<int:pk>/update',views.LicenseUpdate.as_view(),name='license-update'),

    path('customer/<int:pk>/delete',views.CustomerDelete.as_view(),name='customer-delete'),
    path('loanbill/<int:pk>/delete',views.LoanBillDelete.as_view(),name='loanbill-delete'),
    path('loanbill/<int:pk>/delete',views.ReleaseDelete.as_view(),name='release-delete'),
    path('license/<int:pk>/delete',views.LicenseDelete.as_view(),name='license-delete'),
]
