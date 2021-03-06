# Generated by Django 4.0.6 on 2022-07-16 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
                (
                    'previous_status',
                    models.CharField(default='N', max_length=255),
                ),
                ('file', models.FileField(blank=True, upload_to='issue/')),
                ('status', models.CharField(default='N', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=255, blank=False)),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('N', 'New'),
                            ('A', 'Assigned'),
                            ('V', 'Verified'),
                            ('C', 'Closed'),
                            ('H', 'On hold'),
                        ],
                        default='N',
                        max_length=1,
                    ),
                ),
                ('details', models.ManyToManyField(to='issue.detail')),
                (
                    'owner',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='owned_issues',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
