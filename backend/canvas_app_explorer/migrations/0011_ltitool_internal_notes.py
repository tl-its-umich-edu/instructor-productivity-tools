# Generated by Django 3.2.14 on 2022-08-05 20:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas_app_explorer', '0010_alter_ltitool_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ltitool',
            name='internal_notes',
            field=tinymce.models.HTMLField(help_text='a place to put helpful info for admins, not visible to users', null=True),
        ),
    ]
