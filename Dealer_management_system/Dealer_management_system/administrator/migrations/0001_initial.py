# Generated by Django 3.1.2 on 2021-11-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_description', models.TextField()),
                ('Cost', models.FloatField()),
            ],
        ),
    ]
