# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=64)),
                ('last_name', models.CharField(db_index=True, max_length=64)),
                ('middle_name', models.CharField(max_length=32)),
                ('wage', models.DecimalField(db_index=True, decimal_places=2, max_digits=10)),
                ('year', models.IntegerField(db_index=True, default=0)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wages.Agency')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wages.Department')),
                ('government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wages.Government')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wages.Title')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wage',
            unique_together=set([('first_name', 'last_name', 'middle_name', 'government', 'dept', 'title', 'wage', 'year')]),
        ),
    ]
