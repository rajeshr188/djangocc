from django.db import models
from django.shortcuts import reverse
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    #CreatedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    CreatedOn=models.DateTimeField(auto_now=True)
    Name=models.CharField(max_length=30)
    relatedas=(('S/o','S/o'),('D/o','D/o'),('W/o','W/o'))
    RelatedAs=models.CharField(max_length=3,choices=relatedas,default='S/o')
    RelatedTo=models.CharField(max_length=20,default="Relation/name")
    Address=models.TextField(default=".")
    Area=models.CharField(max_length=20,default=".")
    ContactNo=models.CharField(max_length=10,default="911")
    EmailId=models.EmailField(blank=True,null=True)
    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('girvi:customer-detail', args=[str(self.id)])
class License(models.Model):
    #OwnedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    CreatedOn=models.DateTimeField(auto_now=True)
    ltype=(('PBL','Pawn Brokers License'),
            ('GST','Goods & Service Tax'))
    Type=models.CharField(max_length=3,choices=ltype,default='PBL')
    Lid=models.CharField(max_length=20,unique=True,help_text='type Licence name here',default='unlicensed')
    ShopName=models.CharField(max_length=50,help_text='type Shop name Here',default='girvi dukan')
    Address=models.TextField(help_text='type License address here')
    Propreitor=models.CharField(max_length=20,help_text='type owner name here',default='owner')
    class Meta:
        ordering=['CreatedOn']

    def __str__(self):
        return self.Lid

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('girvi:license-detail', args=[str(self.id)])
class LoanBill(models.Model):
    license=models.ForeignKey(License,on_delete=models.CASCADE)
    LoanDate=models.DateTimeField(default=timezone.now)
    LoanId=models.CharField(max_length=10,help_text='loanid here')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    itype=(
            ('Gold','Gold'),
            ('Silver','Silver'),
            ('Bronze','Bronze'),('O','Other'),)
    ItemType=models.CharField(max_length=6,choices=itype,default='Gold')
    ItemDesc=models.TextField(help_text="items here")
    ItemWeight=models.DecimalField(max_digits=7,decimal_places=2,default='0.0')
    LoanAmount=models.DecimalField(max_digits=10,decimal_places=2,default='0')
    ItemValue=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    LoanInt=models.DecimalField(max_digits=7,decimal_places=2,default='2')

    class Meta:
        ordering=['-LoanDate']
        unique_together=('license','LoanId')
    def __str__(self):
            return str(self.id)

    def noofmonths(self):
        cd=datetime.datetime.now()
        nom=(cd.year-self.LoanDate.year)*12 +cd.month-self.LoanDate.month
        if(nom<=0):
            return 1
        else:
            return nom
    def interestdue(self):
        return float(((self.LoanAmount)*self.noofmonths()*(self.LoanInt))/100)

    def total(self):
        return self.interestdue() + float(self.LoanAmount)
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('girvi:loanbill-detail', args=[str(self.id)])

class Release(models.Model):
    loanbill=models.OneToOneField(LoanBill,on_delete=models.CASCADE,primary_key=True,related_name='bill')
    ReleaseId=models.CharField(max_length=10,unique=True)
    ReleaseDate=models.DateTimeField(default=timezone.now)
    #ReleasedBy=models.OneToOne(Customer,on_delete=models.CASCADE)
    InterestPaid=models.DecimalField(max_digits=7,decimal_places=2)
    class Meta:
        ordering=['ReleaseDate']
    def __str__(self):
        return self.ReleaseId
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('girvi:release-detail', args=[str(self.loanbill)])
