from django.shortcuts import render
from .models import LearningJourney, AboutMe

# =====================================
# Views for the Learning Journey App
# =====================================

def index(request):
    """
    Display the homepage showing all learning journey entries.

    This view fetches all records from the LearningJourney model
    and passes them to the 'index.html' template for display in a table.
    """
    journey = LearningJourney.objects.all()
    return render(request, 'index.html', {'journey': journey})


def about_me(request):
    """
    Display the 'About Me' page with user information.

    This view retrieves all records from the AboutMe model
    and renders them in the 'aboutMe.html' template.
    """
    about = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'about': about})
