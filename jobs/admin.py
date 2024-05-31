from django.contrib import admin
from .models import Jobs

class JobAdmin(admin.ModelAdmin):
    list_display = ('job',)
    search_fields = ('job',)


admin.site.register(Jobs, JobAdmin)