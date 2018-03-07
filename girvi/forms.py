from django import forms
from .models import Release,LoanBill,Customer
class LoanBillForm(forms.ModelForm):
    class Meta:
        model=LoanBill
        fields='__all__'
        #widgets={'LoanDate':forms.SplitDateTimeWidget}
    def __init__(self,*args,**kwargs):
        pkid=kwargs.pop('pk')
        super(LoanBillForm,self).__init__(*args,**kwargs)
        if pkid:
            self.fields['customer'].queryset=Customer.objects.filter(id=pkid)
        else:
            self.fields['customer'].queryset=Customer.objects.all()
class ReleaseForm(forms.ModelForm):
    class Meta:
        model=Release
        fields='__all__'
    def __init__(self,*args,**kwargs):
        #user=kwargs.pop('user')
        loan=kwargs.pop('pk')
        super(ReleaseForm,self).__init__(*args,**kwargs)
        if loan:
            self.fields['loanbill'].queryset=LoanBill.objects.filter(id=loan)
        else:
            self.fields['loanbill'].queryset=LoanBill.objects.filter(bill__isnull=True)
