from django.contrib import admin
from .models import (Categoria,Receita, )


class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Receita)
class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'category')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'category__nome') 

admin.site.register(Categoria,CategoriaAdmin);
