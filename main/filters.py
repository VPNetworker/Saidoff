import django_filters
from main import models


class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Projects
        fields = ['title']