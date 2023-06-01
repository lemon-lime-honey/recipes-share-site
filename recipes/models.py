from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='recipe_written')
    content = models.TextField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=10)
    image = ProcessedImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.IntegerField()
    difficulty = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])  # 난이도
    like_recipes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_recipes_users', blank=True)  # 레시피 좋아요
    bookmark = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_users', blank=True)  # 레시피 북마크
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')


    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    detail = models.TextField()


    def __str__(self):
        return self.recipe


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)


class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Equip(models.Model):
#     microwave = models.BooleanField(default=False)
#     stove = models.BooleanField(default=False)
#     oven = models.BooleanField(default=False)
#     air_fryer = models.BooleanField(default=False) 태그