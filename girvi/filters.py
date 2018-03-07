from . models import Customer
import django_filters

class CustomerFilter(django_filters.FilterSet):
    Name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=Customer
        fields=['RelatedTo','ContactNo','Area']
