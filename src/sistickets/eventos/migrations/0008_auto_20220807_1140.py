# Generated by Django 3.0 on 2022-08-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20220805_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='code',
        ),
        migrations.AddField(
            model_name='evento',
            name='codigoqr',
            field=models.CharField(default=False, max_length=2083),
        ),
    ]
