# Generated by Django 4.2.3 on 2023-08-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_remove_good_image_good_published_alter_good_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='product',
            new_name='good',
        ),
    ]