from django.shortcuts import get_object_or_404, render

from .models import Review

def all_reviews(request):

    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
        }

    
    return render(request, 'reviews/reviews.html', context)