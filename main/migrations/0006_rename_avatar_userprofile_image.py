# Generated by Django 5.0.3 on 2024-03-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_certificate_image_alter_portfolio_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='avatar',
            new_name='image',
        ),
    ]