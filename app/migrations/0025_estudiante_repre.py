# Generated by Django 4.0.4 on 2022-05-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_voto_candidato_alter_voto_votacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='repre',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]