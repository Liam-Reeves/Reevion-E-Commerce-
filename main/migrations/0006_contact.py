# Generated by Django 5.1 on 2025-02-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_newsletter_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
