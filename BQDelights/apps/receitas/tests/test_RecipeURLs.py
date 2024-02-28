from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from apps.receitas import views
import pytest

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        ROOT_URLCONF='apps.receitas.urls',
        urlconf = settings.ROOT_URLCONF if hasattr(settings, 'ROOT_URLCONF') else 'apps.receitas.urls'
    )


# Formas de Executar o teste:
# python3 manage.py test apps.receitas.tests
# pytest -rP apps/receitas/tests.py
    
class RecipeURLsTest(TestCase):
      
    def test_home_url_is_correct(self):
        url = reverse('apps.receitas:home')
        self.assertEqual(url,'/')

    def test_categorias_url_is_correct(self):
        url = reverse('apps.receitas:categorias_list',kwargs={'id':1})
        self.assertEqual(url,'/receitas/categorias/1')
    
    def test_detalhes_url_is_correct(self):
        url = reverse('apps.receitas:detalhes',kwargs={'id':1})
        self.assertEqual(url,'/receitas/1/details')
