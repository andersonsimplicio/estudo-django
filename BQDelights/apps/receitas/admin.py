from django.contrib import admin
from .models import Receita
from .models import Categoria as CategoriaReceitas

@admin.register(CategoriaReceitas)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Receita)
class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published','category','author','preparation_steps_is_html')
    list_filter = ('is_published',)
    search_fields = ('title',) 
    list_editable = ('is_published',)


