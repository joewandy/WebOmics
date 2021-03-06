# Generated by Django 2.0.2 on 2018-06-18 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0012_analysis_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='species',
        ),
        migrations.AddField(
            model_name='analysisspecies',
            name='analysis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linker.Analysis'),
        ),
    ]
