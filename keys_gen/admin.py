from django.contrib import admin
from .models import Keys


# Register your models here.


class KeysAdmin(admin.ModelAdmin):
    list_display = ['key', 'created', 'status']
    list_filter = ['status', 'created']


admin.site.register(Keys, KeysAdmin)
