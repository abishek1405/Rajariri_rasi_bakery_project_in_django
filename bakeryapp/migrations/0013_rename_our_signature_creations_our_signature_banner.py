# Generated by Django 5.0.6 on 2024-07-06 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakeryapp', '0012_remove_our_signature_creations_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='our_signature_creations',
            new_name='our_signature_banner',
        ),
    ]
