# Generated by Django 3.1.3 on 2022-06-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0014_questioncount'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
