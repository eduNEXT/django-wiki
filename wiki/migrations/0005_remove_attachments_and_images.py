# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 19:03
from __future__ import absolute_import, unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_increase_slug_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='current_revision',
        ),
        migrations.RemoveField(
            model_name='attachmentrevision',
            name='attachment',
        ),
        migrations.RemoveField(
            model_name='attachmentrevision',
            name='previous_revision',
        ),
        migrations.RemoveField(
            model_name='attachmentrevision',
            name='user',
        ),
        migrations.RemoveField(
            model_name='imagerevision',
            name='revisionpluginrevision_ptr',
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.DeleteModel(
            name='AttachmentRevision',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='ImageRevision',
        ),
    ]
