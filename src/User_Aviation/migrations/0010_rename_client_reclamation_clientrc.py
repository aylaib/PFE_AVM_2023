# Generated by Django 4.1.7 on 2023-05-04 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Aviation', '0009_alter_commandeav_options_alter_clientav_avatar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamation',
            old_name='client',
            new_name='clientRc',
        ),
    ]
