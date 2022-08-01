from django.apps import apps
from django.contrib import admin
from .models import Post

# Register your models here.
models = apps.get_models()

@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = (
    'title', 'slug', 'category', 'region', 'views_count', 'is_interview', "is_inquiry", "is_global", "is_recommended",
    "is_selected", "created_at")
    list_filter = ('region', 'is_interview', 'is_recommended', 'is_selected')
    search_fields = ('title', 'region')
    ordering = ('-updated_at',)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass