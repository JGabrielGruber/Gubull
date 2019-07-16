# Generated by Django 2.1.1 on 2019-01-15 10:40

import animais.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0004_auto_20190112_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bovino',
            name='filho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animais.Filhos'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='foto_dois',
            field=models.FileField(blank=True, null=True, upload_to=animais.models.Bovino.file_path, verbose_name='Segunda Foto'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='foto_quatro',
            field=models.FileField(blank=True, null=True, upload_to=animais.models.Bovino.file_path, verbose_name='Quarta Foto'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='foto_tres',
            field=models.FileField(blank=True, null=True, upload_to=animais.models.Bovino.file_path, verbose_name='Terceira Foto'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='foto_um',
            field=models.FileField(blank=True, null=True, upload_to=animais.models.Bovino.file_path, verbose_name='Foto Principal'),
        ),
    ]
