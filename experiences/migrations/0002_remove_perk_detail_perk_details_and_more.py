# Generated by Django 5.0.6 on 2024-06-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perk',
            name='detail',
        ),
        migrations.AddField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]
