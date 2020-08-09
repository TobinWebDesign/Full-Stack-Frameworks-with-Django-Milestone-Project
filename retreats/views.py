from django.shortcuts import render
from .models import Retreat

# Create your views here.


def all_retreats(request):
    """ A view to show all retreats, including sorting and search queries """

    retreats = Retreat.objects.all()

    context = {
        'retreats': retreats,
    }
    
    return render(request, 'retreats/retreats.html', context)