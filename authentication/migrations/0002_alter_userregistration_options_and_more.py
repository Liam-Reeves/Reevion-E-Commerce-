# Generated by Django 5.1 on 2025-01-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userregistration',
            options={'verbose_name_plural': 'User Registration'},
        ),
        migrations.AddField(
            model_name='userregistration',
            name='email',
            field=models.EmailField(default=True, max_length=200),
        ),
    ]
