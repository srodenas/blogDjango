# Generated by Django 4.0 on 2021-12-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('fecha_eliminación', models.DateField(auto_now_add=True, verbose_name='Fecha de eliminación')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoria')),
                ('imagen_referencial', models.ImageField(upload_to='categoria/', verbose_name='Imagen Referencial')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
