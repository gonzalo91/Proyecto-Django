# Generated by Django 3.0.5 on 2020-05-03 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_collectioncenter_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Web.Categoria'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
