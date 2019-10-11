# Generated by Django 2.2.6 on 2019-10-11 08:48

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
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comission', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Designatedid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr.Category')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr.Subcategory')),
            ],
        ),
    ]