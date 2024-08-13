from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from .models import Building, Subdivision, Specialty, Page, RegisteredPatients, Organization


class SubdivisionInline(admin.TabularInline):
    model = Subdivision
    extra = 1
    verbose_name = "Подразделение"
    verbose_name_plural = "Список подразделений из статистики квазара, относящихся к выбранному корпусу"
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget(attrs={'style': 'width: 500px;'})},
    }


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [SubdivisionInline]
    verbose_name = "Корпус"
    verbose_name_plural = "Корпуса"


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = "Специальность"
    verbose_name_plural = "Специальности"


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'building', 'subdivision')
    list_filter = ('building',)
    search_fields = ('title', 'path', 'building__name', 'subdivision')
    verbose_name = "Страница"
    verbose_name_plural = "Страницы"


@admin.register(RegisteredPatients)
class RegisteredPatientsAdmin(admin.ModelAdmin):
    list_display = (
        'subdivision', 'speciality', 'slots_today', 'free_slots_today', 'slots_14_days', 'free_slots_14_days',
        'report_datetime'
    )
    search_fields = ('subdivision', 'speciality', 'report_datetime')
    verbose_name = "Зарегистрированный пациент"
    verbose_name_plural = "Зарегистрированные пациенты"


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'logo_preview')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 200px;"/>', obj.logo.url)
        return "(No logo)"

    logo_preview.short_description = "Предпросмотр логотипа"
