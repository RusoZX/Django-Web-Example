# Generated by Django 4.1.7 on 2023-03-18 12:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feed", "0002_alter_usuario_created_by"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Usuario",
            new_name="Post",
        ),
    ]
