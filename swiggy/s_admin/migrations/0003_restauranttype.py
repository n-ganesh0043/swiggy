# Generated by Django 2.2.4 on 2020-04-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_admin', '0002_areamodel_citymodel_statemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('type_no', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
    ]