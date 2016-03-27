# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliveryCost',
            field=models.IntegerField(default=0, verbose_name='Стоимость доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='deliveryData',
            field=models.DateField(default=datetime.datetime(2016, 3, 15, 20, 15, 46, 932078, tzinfo=utc), verbose_name='Дата доставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='deliveryMethod',
            field=models.CharField(default='', verbose_name='Способ доставки', choices=[('SD', 'Самовывоз'), ('CD', 'Доставка курьером'), ('PD', 'Доставка почтой')], max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='telefon',
            field=models.CharField(default='', verbose_name='Телефон', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 3, 15, 20, 14, 51, 718606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 3, 15, 20, 14, 51, 719179, tzinfo=utc), verbose_name='Дата размещения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(verbose_name='Имя заказчика', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(verbose_name='Статус заказа', choices=[(-1, 'Аннулирован'), (0, 'В обработке'), (1, 'Собирается'), (2, 'Отправлен в службу доставки'), (3, 'Можно забрать из самовывоза'), (4, 'Выполнен')], max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='summ',
            field=models.FloatField(default=0, verbose_name='Сумма'),
        ),
    ]
