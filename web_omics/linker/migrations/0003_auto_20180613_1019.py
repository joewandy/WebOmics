# Generated by Django 2.0.2 on 2018-06-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0002_experiment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='species',
            field=models.CharField(max_length=100, null=True),
        ),
    ]