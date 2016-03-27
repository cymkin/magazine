# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Имя', max_length=200)),
                ('title', models.CharField(verbose_name='Тема', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('data', models.DateField(default=datetime.datetime(2016, 3, 7, 23, 46, 19, 404907, tzinfo=utc))),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='firstPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='media')),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
            ],
            options={
                'verbose_name': 'Первая запись',
                'verbose_name_plural': 'Первые записи',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('summ', models.FloatField(default=0)),
                ('data', models.DateField(default=datetime.datetime(2016, 3, 7, 23, 46, 19, 405496, tzinfo=utc))),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='secondPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='media')),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('link', models.CharField(verbose_name='Ссылка', max_length=200)),
                ('buttonText', models.CharField(verbose_name='Надпись на кнопке', max_length=30)),
            ],
            options={
                'verbose_name': 'Вторая запись',
                'verbose_name_plural': 'Вторые записи',
            },
        ),
    ]
