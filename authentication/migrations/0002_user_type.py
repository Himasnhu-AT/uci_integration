# Generated by Django 4.2.9 on 2024-01-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=255),
        ),
    ]
