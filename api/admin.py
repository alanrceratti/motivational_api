from django.contrib import admin
from .models import Category, Phrases

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Phrases)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'category_name')
