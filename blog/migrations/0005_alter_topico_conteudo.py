# Generated by Django 5.0.3 on 2024-03-24 02:03

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='conteudo',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description'),
        ),
    ]