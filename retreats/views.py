from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Retreat

# Create your views here.


def all_retreats(request):
    """ A view to show all retreats, including sorting and search queries """

    retreats = Retreat.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('retreats'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            retreats = retreats.filter(queries)

    context = {
        'retreats': retreats,
        'search_term': query,
    }
    
    return render(request, 'retreats/retreats.html', context)

def retreat_detail(request, retreat_id):
    """ A view to show idividual retreats """

    retreat = get_object_or_404(Retreat, pk=retreat_id)

    context = {
        'retreat': retreat,
    }
    
    return render(request, 'retreats/retreat_detail.html', context)