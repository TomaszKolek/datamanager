from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render

from budgetportal.models import (
    Department,
    FinancialYear,
    Government,
    Programme,
    Sphere,
)


class FinancialYearAdmin(admin.ModelAdmin):
    pass


class SphereAdmin(admin.ModelAdmin):
    pass


class GovernmentAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'vote_number',
        'name',
        'get_government',
        'get_sphere',
        'get_financial_year',
    )
    list_display_links = (
        'vote_number',
        'name',
    )
    list_filter = (
        'government__sphere__financial_year__slug',
        'government__sphere__name',
        'government__name',
    )
    search_fields = (
        'government__sphere__financial_year__slug',
        'government__sphere__name',
        'government__name',
        'name',
    )

    def get_government(self, obj):
        return obj.government.name

    def get_sphere(self, obj):
        return obj.government.sphere.name

    def get_financial_year(self, obj):
        return obj.government.sphere.financial_year.slug


class ProgrammeAdmin(admin.ModelAdmin):
    pass


@admin.site.register_view('entity_datasets', 'Entity Datasets')
def my_view(request, *args, **kwargs):
    return render(request, 'admin/entity_datasets.html', {
        'financial_years': FinancialYear.objects.all(),
    })


admin.site.register(FinancialYear, FinancialYearAdmin)
admin.site.register(Sphere, SphereAdmin)
admin.site.register(Government, GovernmentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Programme, ProgrammeAdmin)
