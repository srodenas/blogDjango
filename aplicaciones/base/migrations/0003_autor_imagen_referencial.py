# Generated by Django 4.0 on 2021-12-29 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_autor_contacto_redessociales_supcriptor_web_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='imagen_referencial',
            field=models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Imagen del autor'),
        ),
    ]
