# Generated by Django 2.1.5 on 2019-07-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20190706_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='categoria',
            field=models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre')], max_length=1),
        ),
        migrations.AlterField(
            model_name='productos',
            name='subcategoria',
            field=models.CharField(choices=[('business', 'business'), ('casual', 'casual'), ('chamarra', 'chamarra'), ('shoes', 'shoes'), ('tshirt', 'tshirt')], max_length=1),
        ),
    ]