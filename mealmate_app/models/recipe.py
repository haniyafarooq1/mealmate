from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()
    estimated_time = models.IntegerField(help_text="Time in minutes")

    def __str__(self):
        return self.title
