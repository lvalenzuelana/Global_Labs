# Generated by Django 3.2.10 on 2022-02-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_alter_papers_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='file',
            field=models.CharField(max_length=1024),
        ),
    ]
