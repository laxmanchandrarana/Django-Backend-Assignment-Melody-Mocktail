from django.contrib import admin
from .models import Redirect

@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = ('title_web', 'title_phone', 'position', 'is_active', 'availability')
    list_filter = ('is_active', 'availability')
    search_fields = ('title_web', 'title_phone')