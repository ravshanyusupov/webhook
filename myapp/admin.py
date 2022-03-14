from django.contrib import admin
from .models import Kimyo, Users


class Filter(admin.ModelAdmin):
    list_filter = ('test_name', 'date')


admin.site.register(Kimyo)
admin.site.register(Users, Filter)
