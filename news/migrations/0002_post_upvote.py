# Generated by Django 3.0.6 on 2020-05-15 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]
