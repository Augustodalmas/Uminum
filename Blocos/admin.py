from django.contrib import admin
from Blocos.models import Produto, Serie, Formato

class produtoAdmin(admin.ModelAdmin):
    list_display = ('Job',)
    search_fields = ('Job',)


class serieAdmin(admin.ModelAdmin):
    list_display = ('Serie',)
    search_fields = ('Serie',)


class formatoAdmin(admin.ModelAdmin):
    list_display = ('formato',)
    search_fields = ('formato',)

admin.site.register(Produto, produtoAdmin),
admin.site.register(Serie, serieAdmin),
admin.site.register(Formato, formatoAdmin)