# Generated by Django 3.0 on 2022-08-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='lugar',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
