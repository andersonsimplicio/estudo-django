from django.test import TestCase
from django.conf import settings
from django.urls import reverse,resolve
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
        #urlconf = settings.ROOT_URLCONF if hasattr(settings, 'ROOT_URLCONF') else 'apps.receitas.urls'
    )

# Formas de Executar o teste:
# python3 manage.py test apps.receitas.tests
# pytest -rP apps/receitas/tests.py

class ReceitaViewsTest(TestCase):
    def test_receita_home_is_corretc(self):
        view = resolve(reverse('apps.receitas:home'))
        self.assertIs(view.func,views.home)
    
    def test_receita_categoria_is_corretc(self):
        view = resolve(reverse('apps.receitas:categorias_list',kwargs={'id':1}))
        self.assertIs(view.func,views.categorias_view)
    
    def test_receita_detalhes_is_corretc(self):
        view = resolve(reverse('apps.receitas:detalhes',kwargs={'id':1}))
        self.assertIs(view.func,views.receitas_view)

    