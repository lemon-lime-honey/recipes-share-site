# Generated by Django 3.2.18 on 2023-05-26 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_alter_recipereview_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='book_mark',
        ),
        migrations.AddField(
            model_name='recipe',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
