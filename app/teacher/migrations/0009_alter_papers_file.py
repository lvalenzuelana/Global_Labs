# Generated by Django 3.2.10 on 2022-02-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_auto_20220212_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='file',
            field=models.FileField(max_length=1024, upload_to=''),
        ),
    ]
