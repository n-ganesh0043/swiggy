# Generated by Django 2.2.4 on 2020-04-15 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statemodel',
            fields=[
                ('state_no', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Citymodel',
            fields=[
                ('city_no', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.Statemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Areamodel',
            fields=[
                ('area_no', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.Citymodel')),
            ],
        ),
    ]