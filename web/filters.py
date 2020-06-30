import django_filters
from .models import *


class PengaduanFilter(django_filters.FilterSet):
    class Meta:
        model = Penanganan
        fields = '__all__'
