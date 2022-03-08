import django_filters
from django.db.models import CharField

from .models import Community


class CommunityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    # creation_date = django_filters.NumberFilter(field_name='creation_date', lookup_expr='year')
    creation_date__gt = django_filters.NumberFilter(field_name='creation_date', lookup_expr='year__gt')
    creation_date__lt = django_filters.NumberFilter(field_name='creation_date', lookup_expr='year__lt')

    class Meta:
        model = Community
        fields = ['name', 'size', 'cool', 'smelliness']
