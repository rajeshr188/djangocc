from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Customer,License,Release,LoanBill
from . forms import ReleaseForm,LoanBillForm
from django.db.models import Avg,Sum
from easy_pdf.views import PDFTemplateView,PDFTemplateResponseMixin
from crispy_forms.helper import FormHelper
# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    loanbills=LoanBill.objects.all()
    num_customers=Customer.objects.all().count()
    num_loanbills=loanbills.count()
    num_licenses=License.objects.all().count()
    num_pendingbills=num_loanbills-Release.objects.all().count()
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1

    totalLoan=loanbills.aggregate(total=Sum('LoanAmount'))
    totalgla=loanbills.filter(ItemType='gold').aggregate(total=Sum('LoanAmount'))
    totalsla=loanbills.filter(ItemType='silver').aggregate(total=Sum("LoanAmount"))
    totalbla=loanbills.filter(ItemType='Bronze').aggregate(total=Sum('LoanAmount'))
    #totalint=LoanBill.objects.filter(Licence__OwnedBy=request.user).aggregate(total=Sum('interestdue'))
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_licenses':num_licenses,
        'num_customers':num_customers,'num_loanbills':num_loanbills,'num_visits':num_visits,'totalLoan':totalLoan,'totalgla':totalgla,
        'totalsla':totalsla,'totalbla':totalbla},
    )

class LedgerListView(generic.ListView):
    model=LoanBill
    template_name='girvi/ledger_list.html'
    paginate_by=50

class CustomerListView(generic.ListView):
    model=Customer
    paginate_by=100

class LoanBillListView(generic.ListView):
    model=LoanBill
    paginate_by=100

from django.views.generic.dates import YearArchiveView

class LoanBillYearArchiveView(YearArchiveView):
    queryset=LoanBill.objects.all()
    date_field='LoanDate'
    make_object_list=True
from django.views.generic.dates import MonthArchiveView
class LoanBillMonthArchiveView(MonthArchiveView):
    queryset=LoanBill.objects.all()
    date_field='LoanDate'
    make_object_list=True

class LicenseListView(generic.ListView):
    model=License

class ReleaseListView(generic.ListView):
    model=Release

class CustomerDetailView(generic.DetailView):
    model=Customer
    def get_context_data(self,**kwargs):
        context=super(CustomerDetailView,self).get_context_data(**kwargs)
        cl=LoanBill.objects.filter(customer=self.kwargs['pk'])
        context['totalla']=cl.aggregate(t=Sum('LoanAmount'))
        context['totalgw']=cl.filter(ItemType='Gold').aggregate(t=Sum('ItemWeight'))
        context['totalsw']=cl.filter(ItemType='Silver').aggregate(t=Sum('ItemWeight'))
        context['totalbw']=cl.filter(ItemType='Bronze').aggregate(t=Sum('ItemWeight'))

        return context

class LicenseDetailView(generic.DetailView):
    model=License
    def get_context_data(self,**kwargs):
        context=super(LicenseDetailView,self).get_context_data(**kwargs)
        cl=License.objects.filter(id=self.kwargs['pk'])
        context['tla']=cl.aggregate(t=Sum('loanbill__LoanAmount'))
        tla=context['tla']
        context['urloan']=LoanBill.objects.filter(license=self.kwargs['pk']).exclude(bill__isnull=False).count()
        context['urtla']=LoanBill.objects.filter(license=self.kwargs['pk']).exclude(bill__isnull=False).aggregate(t=Sum('LoanAmount'))
        context['rtla']=LoanBill.objects.filter(license=self.kwargs['pk']).exclude(bill__isnull=True).aggregate(t=Sum('LoanAmount'))
        context['urtglw']=LoanBill.objects.filter(license=self.kwargs['pk'],ItemType='Gold').exclude(bill__isnull=False).aggregate(t=Sum('ItemWeight'))
        context['tglw']=LoanBill.objects.filter(license=self.kwargs['pk'],ItemType='Gold').aggregate(t=Sum('ItemWeight'))
        tglw=context['tglw']
        context['avg']=int(tla['t']/tglw['t'])
        return context
class LoanBillDetailView(generic.DetailView):
    model=LoanBill

class PDFLoanBillDetailView(PDFTemplateResponseMixin,generic.DetailView):
    model=LoanBill
    template_name='girvi/loanbill_detail_pdf.html'
#class LoanBillDetailPDFView(PDFTemplateView):
#    template_name='girvi/billprint.html'
#    def get_context_data(self, **kwargs):
#        return super(HelloPDFView, self).get_context_data(
#            pagesize='A5',
##            **kwargs
#        )

class ReleaseDetailView(generic.DetailView):
    model=Release

class LicenseCreate(CreateView):
    model=License
    fields='__all__'
    initial={'LType':'PBL'}

class LicenseUpdate(UpdateView):
    model=License
    fields='__all__'
class LicenseDelete(DeleteView):
    model=License
    success_url = reverse_lazy('girvi:license-list')
#Customer Forms
class CustomerCreate(CreateView):
    model=Customer
    fields='__all__'

class CustomerUpdate(UpdateView):
    model=Customer
    fields='__all__'
class CustomerDelete(DeleteView):
    model=Customer
    success_url = reverse_lazy('girvi:customer-list')

#Loan Forms
class LoanBillCreate(CreateView):
    form_class=LoanBillForm
    template_name='girvi/loanbill_form.html'
    def get_form_kwargs(self):
        kwargs = super(LoanBillCreate, self).get_form_kwargs()
        if self.kwargs:
            kwargs['pk']=self.kwargs['pk']
        else: kwargs['pk']=''
        return kwargs


class LoanBillUpdate(UpdateView):
    model=LoanBill
    fields='__all__'
class LoanBillDelete(DeleteView):
    model=LoanBill
    success_url = reverse_lazy('girvi:loanbill-list')

#RElease Forms
class ReleaseCreate(CreateView):
    form_class=ReleaseForm
    template_name='girvi/release_form.html'

    def get_form_kwargs(self):
        kwargs = super(ReleaseCreate,self).get_form_kwargs()
        if self.kwargs:
            kwargs['pk']=self.kwargs['pk']
        else:
            kwargs['pk']=''
        #kwargs['user']=self.request.user
        return kwargs

class ReleaseUpdate(UpdateView):
    model=Release
    fields='__all__'

class ReleaseDelete(DeleteView):
    model=Release
    success_url = reverse_lazy('girvi:release-list')
