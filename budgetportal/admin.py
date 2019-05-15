from django.contrib import admin
from django.views.generic import TemplateView
from import_export.formats import base_formats
from import_export.admin import ImportExportModelAdmin, ImportForm, ImportMixin, ConfirmImportForm
from django.core.exceptions import ValidationError
from import_export.fields import Field
from django import forms
from django.utils.text import slugify

from budgetportal.models import (
    Department,
    FinancialYear,
    Government,
    GovtFunction,
    Programme,
    Sphere,
)
from budgetportal.bulk_upload import bulk_upload_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.utils import ProgrammingError
from django.contrib import messages
import logging

from .import_export_admin import (
    CustomIsVotePrimaryWidget,
    CustomGovernmentWidget,
    DepartmentInstanceLoader,
    DepartmentResource
)


logger = logging.getLogger(__name__)
admin.site.login = login_required(admin.site.login)


class FinancialYearAdmin(admin.ModelAdmin):
    pass


class SphereAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class GovernmentAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class GovtFunctionAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class CustomImportForm(ImportForm):
    sphere = forms.ModelChoiceField(
        queryset=Sphere.objects.all(),
        required=True
    )

class CustomConfirmImportForm(ConfirmImportForm):
    sphere = forms.ModelChoiceField(
        queryset=Sphere.objects.all(),
        required=True
    )

class CustomCSV(base_formats.TextFormat):
    TABLIB_MODULE = 'tablib.formats._csv'
    CONTENT_TYPE = 'text/csv'

    def create_dataset(self, in_stream, **kwargs):
        # The package does the below which doesn't work
        # if sys.version_info[0] < 3:
            # python 2.7 csv does not do unicode
            # return super(CSV, self).create_dataset(in_stream.encode('utf-8'), **kwargs)
        # return super(CSV, self).create_dataset(in_stream, **kwargs)
        return super(CustomCSV, self).create_dataset(in_stream, **kwargs)


class DepartmentAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DepartmentResource
    formats = ( CustomCSV, )

    def get_import_form(self):
        return CustomImportForm

    def get_confirm_import_form(self):
        return CustomConfirmImportForm

    def get_resource_kwargs(self, request, *args, **kwargs):
        if hasattr(self, 'sphere'):
            return {'sphere': self.sphere}
        if u'sphere' in request.POST:
            print('sphere ', request.POST[u'sphere'])
            self.sphere = request.POST[u'sphere']
            return {'sphere': request.POST[u'sphere']}
        return {}

    def get_form_kwargs(self, form, *args, **kwargs):
        # pass on `sphere` to the kwargs for the custom confirm form
        if isinstance(form, CustomImportForm):
            if form.is_valid():
                sphere = form.cleaned_data['sphere']
                kwargs.update({'sphere': sphere.id})
        return kwargs

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
    readonly_fields = ('slug',)
    list_per_page = 20

    def get_government(self, obj):
        return obj.government.name

    def get_sphere(self, obj):
        return obj.government.sphere.name

    def get_financial_year(self, obj):
        return obj.government.sphere.financial_year.slug


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = (
        'programme_number',
        'name',
        'get_department',
        'get_government',
        'get_sphere',
        'get_financial_year',
    )
    list_display_links = (
        'programme_number',
        'name',
    )
    list_filter = (
        'department__government__sphere__financial_year__slug',
        'department__government__sphere__name',
        'department__government__name',
        'department__name',
    )
    search_fields = (
        'department__government__sphere__financial_year__slug',
        'department__government__sphere__name',
        'department__government__name',
        'department__name',
        'name',
    )
    readonly_fields = ('slug',)

    def get_department(self, obj):
        return obj.department.name

    def get_government(self, obj):
        return obj.department.government.name

    def get_sphere(self, obj):
        return obj.department.government.sphere.name

    def get_financial_year(self, obj):
        return obj.department.government.sphere.financial_year.slug


class EntityDatasetsView(TemplateView):
    template_name = "admin/entity_datasets.html"
    financial_year_slug = None
    sphere_slug = None

    def get_context_data(self, **kwargs):
        sphere = Sphere.objects.get(
            financial_year__slug=self.financial_year_slug,
            slug=self.sphere_slug,
        )
        return {
            'sphere': sphere,
        }


class UserAdmin(admin.ModelAdmin):
    pass


class SiteAdmin(admin.ModelAdmin):
    pass


admin.site.register_view('bulk_upload', 'Bulk Upload', view=bulk_upload_view)


try:
    for financial_year in FinancialYear.objects.all():
        for sphere in financial_year.spheres.all():
            view = EntityDatasetsView.as_view(
                financial_year_slug=financial_year.slug,
                sphere_slug=sphere.slug,
            )
            path = "%s/%s/entity_datasets" % (financial_year.slug, sphere.slug)
            label = "Entity Datasets - %s %s" % (financial_year.slug, sphere.name)
            admin.site.register_view(path, label, view=view)
except ProgrammingError, e:
    logging.error(e, exc_info=True)


admin.site.register(FinancialYear, FinancialYearAdmin)
admin.site.register(Sphere, SphereAdmin)
admin.site.register(Government, GovernmentAdmin)
admin.site.register(GovtFunction, GovtFunctionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Site, SiteAdmin)
