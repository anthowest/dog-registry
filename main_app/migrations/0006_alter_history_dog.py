# Generated by Django 4.1.1 on 2022-10-05 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_history_year_recognized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historys', to='main_app.dog'),
        ),
    ]
