# Generated by Django 5.0.3 on 2024-03-22 13:19

import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_avatar_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactprofile',
            name='message',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='body',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='body',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='contactprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
    ]
