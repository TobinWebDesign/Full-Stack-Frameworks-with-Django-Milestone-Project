from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Retreat, Category
from .forms import RetreatForm
# Create your views here.


def all_retreats(request):
    """ A view to show all retreats, including sorting and search queries """

    retreats = Retreat.objects.all()
    categories = None
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            retreats = retreats.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'current_categories': categories,
    }
    
    return render(request, 'retreats/retreats.html', context)

def retreat_detail(request, retreat_id):
    """ A view to show idividual retreats """

    retreat = get_object_or_404(Retreat, pk=retreat_id)

    context = {
        'retreat': retreat,
    }
    
    return render(request, 'retreats/retreat_detail.html', context)

def add_retreat(request):
    """ Add a retreat to the store """
    if request.method == 'POST':
        form = RetreatForm(request.POST, request.FILES)
        if form.is_valid():
            retreat = form.save()
            messages.success(request, 'Yey! Successfully added retreat!')
            return redirect(reverse('retreat_detail', args=[retreat.id]))
        else:
            messages.error(request, 'Opps! Failed to add retreat. Please ensure the form is valid.')
    else:
        form = RetreatForm()

    template = 'retreats/add_retreat.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_retreat(request, retreat_id):
    """ Edit a retreat in the store """
    retreat = get_object_or_404(Retreat, pk=retreat_id)
    if request.method == 'POST':
        form = RetreatForm(request.POST, request.FILES, instance=retreat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yey! Successfully updated retreat!')
            return redirect(reverse('retreat_detail', args=[retreat.id]))
        else:
            messages.error(request, 'Opps! Failed to update retreat. Please ensure the form is valid.')
    else:
        form = RetreatForm(instance=retreat)
        messages.info(request, f'You are editing {retreat.name}')

    template = 'retreats/edit_retreat.html'
    context = {
        'form': form,
        'retreat': retreat,
    }

    return render(request, template, context)

def delete_retreat(request, retreat_id):
    """ Delete a retreat from the store """
    retreat = get_object_or_404(Retreat, pk=retreat_id)
    retreat.delete()
    messages.success(request, 'Retreat deleted!')
    return redirect(reverse('retreats'))