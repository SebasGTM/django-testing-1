# Generated by Django 4.1.2 on 2022-10-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isactive',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
