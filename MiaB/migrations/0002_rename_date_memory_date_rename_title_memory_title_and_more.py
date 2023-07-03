# Generated by Django 4.0.4 on 2022-06-08 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MiaB', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memory',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='BodyText',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='MemoryID',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='UserID',
        ),
        migrations.AddField(
            model_name='memory',
            name='bodyText',
            field=models.TextField(default='Hello, world.'),
        ),
        migrations.AddField(
            model_name='memory',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='memories', to=settings.AUTH_USER_MODEL),
        ),
    ]