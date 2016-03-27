# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0002_auto_20160315_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Address',
            field=models.CharField(max_length=300, verbose_name='Адрес', default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentMethod',
            field=models.CharField(max_length=100, verbose_name='Способ оплаты', choices=[('qiwi', 'Visa QIWI Wallet'), ('наличка', 'Наличными')], default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='qiwiAccNumber',
            field=models.CharField(max_length=20, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 3, 25, 16, 6, 4, 38637, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateField(verbose_name='Дата размещения', default=datetime.datetime(2016, 3, 25, 16, 6, 4, 39216, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryMethod',
            field=models.CharField(max_length=20, verbose_name='Способ доставки', choices=[('Самовывоз', 'Самовывоз'), ('Курьер', 'Доставка курьером'), ('Почта', 'Доставка почтой')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=200, verbose_name='Статус заказа', choices=[('Аннулирован', 'Аннулирован'), ('В обработке', 'В обработке'), ('Собирается', 'Собирается'), ('В доставке', 'Отправлен в службу доставки'), ('В самовывозе', 'Можно забрать из самовывоза'), ('Выполнен', 'Выполнен')], default='В обработке'),
        ),
    ]
