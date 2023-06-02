# Generated by Django 3.2.18 on 2023-06-02 08:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_auto_20230602_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='bookmark_users',
            field=models.ManyToManyField(blank=True, related_name='bookmark_recipes', through='recipes.BookmarkRecipe', to=settings.AUTH_USER_MODEL),
        ),
    ]
