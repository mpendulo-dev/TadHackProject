# Generated by Django 3.2.5 on 2021-09-25 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210925_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='ID_Document',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='proof_of_residence',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='qualification',
        ),
    ]
