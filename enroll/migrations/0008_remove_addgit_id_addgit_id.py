# Generated by Django 4.0.1 on 2022-01-21 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_remove_addgit_git_id_addgit_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addgit',
            name='ID',
        ),
        migrations.AddField(
            model_name='addgit',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
