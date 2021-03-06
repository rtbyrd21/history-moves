# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=128, null=True, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=128, null=True, verbose_name="address cont'd")),
                ('city', models.CharField(default='Brooklyn', max_length=64, verbose_name='city')),
                ('state', models.CharField(default='NY', max_length=2, verbose_name='state')),
                ('zip_code', models.CharField(blank=True, default='112', max_length=5, null=True, verbose_name='zip code')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extract', models.CharField(max_length=201)),
                ('beginning_time', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interviews.Address')),
                ('images', models.ManyToManyField(blank=True, to='interviews.Images')),
            ],
        ),
        migrations.CreateModel(
            name='MapFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('event', models.ManyToManyField(blank=True, to='interviews.Event')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedStages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedThings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='map_features',
            field=models.ManyToManyField(blank=True, to='interviews.MapFeatures'),
        ),
        migrations.AddField(
            model_name='location',
            name='neighborhood',
            field=models.ManyToManyField(blank=True, null=True, to='interviews.Neighborhoods'),
        ),
        migrations.AddField(
            model_name='location',
            name='place_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interviews.PlaceCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(blank=True, to='interviews.Images'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ManyToManyField(blank=True, to='interviews.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.ManyToManyField(blank=True, to='interviews.RelatedPeople'),
        ),
        migrations.AddField(
            model_name='event',
            name='stage',
            field=models.ManyToManyField(blank=True, to='interviews.RelatedStages'),
        ),
        migrations.AddField(
            model_name='event',
            name='themes',
            field=models.ManyToManyField(blank=True, to='interviews.Themes'),
        ),
        migrations.AddField(
            model_name='event',
            name='things',
            field=models.ManyToManyField(blank=True, to='interviews.RelatedThings'),
        ),
        migrations.AddField(
            model_name='event',
            name='years',
            field=models.ManyToManyField(blank=True, to='interviews.RelatedYears'),
        ),
    ]
