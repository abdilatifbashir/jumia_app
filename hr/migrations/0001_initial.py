# Generated by Django 2.2.6 on 2019-10-11 12:55

import computed_property.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=400)),
                ('shipping', models.FloatField(blank=True)),
                ('commision', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('shipping', computed_property.fields.ComputedFloatField(blank=True, compute_from='shipping', editable=False)),
                ('category', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='hr.Category')),
                ('sub_category', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='hr.Sub_category')),
            ],
        ),
    ]
