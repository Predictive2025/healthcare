# Generated by Django 5.1.4 on 2025-01-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Predictiveapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='message',
            new_name='notmessage',
        ),
        migrations.RenameField(
            model_name='pharmacistmodel',
            old_name='cerfificate',
            new_name='certificate',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='Request',
            new_name='request',
        ),
    ]
