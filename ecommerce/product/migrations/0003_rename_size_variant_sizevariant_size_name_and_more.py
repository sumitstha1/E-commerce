# Generated by Django 4.1.6 on 2023-02-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_colorvariant_sizevariant_product_color_variant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sizevariant',
            old_name='size_variant',
            new_name='size_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='product.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='product.sizevariant'),
        ),
    ]
