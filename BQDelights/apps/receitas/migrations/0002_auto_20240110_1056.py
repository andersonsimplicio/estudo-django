# Generated by Django 3.1.3 on 2024-01-10 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='author',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Receita',
        ),
    ]