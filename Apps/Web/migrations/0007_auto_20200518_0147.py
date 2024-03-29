# Generated by Django 3.0.5 on 2020-05-18 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Web', '0006_auto_20200503_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioncenter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='collection_center', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.PositiveSmallIntegerField(choices=[('n', 'Nuevo'), ('u', 'Usado')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Producto'), (2, 'Servicio'), (3, 'Medicina')]),
        ),
    ]
