# Generated by Django 4.0.4 on 2022-05-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_voto_votacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='cargo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
