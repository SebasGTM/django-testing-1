# Generated by Django 4.1.2 on 2022-10-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_summery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
