from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    name = models.CharField(max_length=65)
    class Meta:
        verbose_name = 'Categoria' 
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name
    
class Receita(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='produto/covers/%Y/%m/%d/')
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True,blank = True,default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank = True,default=None)
    
    class Meta:
        verbose_name = 'Receita' 
        verbose_name_plural = 'Receitas'
    
    def __str__(self) -> str:
        return self.title


