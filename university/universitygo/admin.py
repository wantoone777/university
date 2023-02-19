from django.contrib import admin

from .models import *


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'location')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'slug', 'summary', 'location', 'avg_price', 'avg_score', 'text_history', 'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4', 'paragraph5', 'subject1', 'subject2', 'subject3', 'subject4', 'subject5', 'phone', 'website', 'img1', 'unv_type', 'time_create', 'time_update', 'after', 'who_is_creator')
    readonly_fields = ('time_create', 'time_update')


class UniversityTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'isMilitary')
    list_display_links = ('id', 'isMilitary')
    search_fields = ('isMilitary',)
    prepopulated_fields = {"slug": ("isMilitary",)}


class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator')
    list_display_links = ('id', 'creator')
    search_fields = ('creator',)
    prepopulated_fields = {"slug": ("creator",)}


class UniversityLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    list_display_links = ('id', 'location')
    search_fields = ('location',)
    prepopulated_fields = {"slug": ("location",)}


class UniversitySubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(University, UniversityAdmin)
admin.site.register(UniversityType, UniversityTypeAdmin)
admin.site.register(UniversitySubject, UniversitySubjectAdmin)
admin.site.register(UniversityLocation, UniversityLocationAdmin)
admin.site.register(Creator, CreatorAdmin)

