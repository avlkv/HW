# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_remove_book_number_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Название книги', 'verbose_name_plural': 'Книги'},
        ),
    ]