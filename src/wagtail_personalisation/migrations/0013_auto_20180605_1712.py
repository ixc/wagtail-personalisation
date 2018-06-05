# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0012_remove_personalisablepagemetadata_is_segmented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_dayrule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='devicerule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_devicerule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='personalisablepagemetadata',
            name='segment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_metadata', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_queryrule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='referralrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_referralrule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='timerule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_timerule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='userisloggedinrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_userisloggedinrule_related', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='visitcountrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_visitcountrule_related', to='wagtail_personalisation.Segment'),
        ),
    ]
