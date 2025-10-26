from django.db import models

# Create your models here.
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)
    passion = models.TextField()

    def __str__(self):
        return self.name