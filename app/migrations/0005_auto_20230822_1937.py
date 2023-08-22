# Generated by Django 3.2.20 on 2023-08-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230822_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='tags',
        ),
        migrations.AddField(
            model_name='booking',
            name='preference',
            field=models.CharField(choices=[('radio', 'radio'), ('talking', 'talking'), ('silence', 'silence'), ('not fused', 'not fused')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='design',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]