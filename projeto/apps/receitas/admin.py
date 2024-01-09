from django.contrib import admin
from .models import (Categoria,Receita, )


class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Receita)
class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'category','author')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'category__nome') 
    list_editable = ('is_published',)

admin.site.register(Categoria,CategoriaAdmin);
