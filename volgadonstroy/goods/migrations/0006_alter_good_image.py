# Generated by Django 4.2.3 on 2023-07-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_category_good_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(default='goods/2023/07/25/no-image-icon-23485.png', upload_to='goods/%Y/%m/%d'),
        ),
    ]