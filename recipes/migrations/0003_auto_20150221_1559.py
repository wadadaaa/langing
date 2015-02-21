# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20140904_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order_index'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={'ordering': ['order', 'id'], 'verbose_name': 'Direction', 'verbose_name_plural': 'Directions'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['name_sorted'], 'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='foodgroup',
            options={'ordering': ['name'], 'verbose_name': 'FoodGroup', 'verbose_name_plural': 'FoodGroups'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['direction', 'order_index', 'id'], 'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='prepmethod',
            options={'ordering': ['-name'], 'verbose_name': 'Preparation Method', 'verbose_name_plural': 'Preparation Methods'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title'], 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipies'},
        ),
        migrations.AlterModelOptions(
            name='servingstring',
            options={'verbose_name': 'Serving String', 'verbose_name_plural': 'Serving Strings'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['name'], 'verbose_name': 'Source', 'verbose_name_plural': 'Sources'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['name'], 'verbose_name': 'Unit', 'verbose_name_plural': 'Units'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text=b'Maximum 120 characters', unique=True, max_length=120, verbose_name='Category|name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direction',
            name='text',
            field=models.TextField(verbose_name='Direction|text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Food|name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='name_sorted',
            field=models.CharField(default=b'', max_length=150, verbose_name='Food|name_sorted'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodgroup',
            name='name',
            field=models.CharField(max_length=150, verbose_name='FoodGroup|name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(null=True, verbose_name='Ingredient|amount', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=200, verbose_name='Photo|caption'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prepmethod',
            name='name',
            field=models.CharField(max_length=60, verbose_name='PrepMethod|name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Recipe|description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='summary',
            field=models.CharField(max_length=500, verbose_name='Recipe|summary', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Recipe|title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servingstring',
            name='text',
            field=models.CharField(max_length=50, verbose_name='ServingString|text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Source|name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(unique=True, max_length=60, verbose_name='Unit|name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name_abbrev',
            field=models.CharField(max_length=60, verbose_name='Unit|name_abbrev', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='plural_abbrev',
            field=models.CharField(max_length=60, verbose_name='Unit|plural_abbrev', blank=True),
            preserve_default=True,
        ),
    ]
