from django.contrib import admin

from data.models import Code


class Codes(admin.ModelAdmin):
    list_display = ('id', 'title', 'code_description', 'file',)
    list_display_links = ('id', 'title', 'file', )
    search_fields = ('id', 'title', )
    list_per_page = 20

admin.site.register(Code, Codes)
