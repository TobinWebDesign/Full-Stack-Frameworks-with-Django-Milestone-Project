from django.shortcuts import render, get_object_or_404
from .models import Retreat

# Create your views here.


def all_retreats(request):
    """ A view to show all retreats, including sorting and search queries """

    retreats = Retreat.objects.all()

    context = {
        'retreats': retreats,
    }
    
    return render(request, 'retreats/retreats.html', context)

def retreat_detail(request, retreat_id):
    """ A view to show idividual retreats """

    retreat = get_object_or_404(Retreat, pk=retreat_id)

    context = {
        'retreat': retreat,
    }
    
    return render(request, 'retreats/retreat_detail.html', context)