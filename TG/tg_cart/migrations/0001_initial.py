# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tg_user', '0001_initial'),
        ('tg_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_user.UserInfo')),
            ],
        ),
    ]