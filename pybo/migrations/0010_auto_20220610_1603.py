# Generated by Django 3.1.3 on 2022-06-10 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_auto_20220610_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='view',
        ),
        migrations.AlterField(
            model_name='questioncount',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_count', to='pybo.question'),
        ),
    ]
