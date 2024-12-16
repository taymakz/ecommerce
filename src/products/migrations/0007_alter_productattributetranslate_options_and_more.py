# Generated by Django 5.1.3 on 2024-12-15 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productclass_abstract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productattributetranslate',
            options={'verbose_name_plural': 'translation of product attributes'},
        ),
        migrations.AlterModelOptions(
            name='productattributevaluetranslate',
            options={'verbose_name_plural': 'translation of product attribute value'},
        ),
        migrations.AlterModelOptions(
            name='productclass',
            options={'verbose_name_plural': 'product classes'},
        ),
        migrations.AlterModelOptions(
            name='producttranslate',
            options={'verbose_name_plural': 'translation of products'},
        ),
    ]
