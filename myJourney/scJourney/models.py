from django.db import models

# =====================================
# Models for the Learning Journey App
# =====================================

class LearningJourney(models.Model):
    """
    Represents an individual entry in the user's learning journey.

    Attributes:
        title (CharField): The title or phase of the learning experience.
        description (TextField): A detailed explanation of what was learned or achieved.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """Return the title of the learning journey entry as its string representation."""
        return self.title


class AboutMe(models.Model):
    """
    Stores personal information about the user.

    Attributes:
        name (CharField): The user's full name.
        age (IntegerField): The user's age.
        education (CharField): The user's educational background.
        passion (TextField): A description of the user's interests or passions.
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)
    passion = models.TextField()

    def __str__(self):
        """Return the user's name as the string representation."""
        return self.name
