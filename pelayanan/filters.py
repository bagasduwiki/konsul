import django_filters
from .models import *

class PelayananFilter(django_filters.FilterSet):
    class Meta:
        model = Pengaduan
        fields = '__all__'
