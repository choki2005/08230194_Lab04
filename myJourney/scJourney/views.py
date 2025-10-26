from django.shortcuts import render
from .models import LearningJourney, AboutMe
# Create your views here.
def index(request):
    journey = LearningJourney.objects.all()
    return render(request, 'index.html', {'journey': journey})

def about_me(request):
    about = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'about': about})
