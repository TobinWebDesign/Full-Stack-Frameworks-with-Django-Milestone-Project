from django.shortcuts import get_object_or_404, render

from .models import Review
from .forms import ReviewForm

def all_reviews(request):

    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
        }

    return render(request, 'reviews/reviews.html', context)

def review_detail(request, review_id):
    """ A view to show idividual reviews """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }
    
    return render(request, 'reviews/review_detail.html', context)

def add_review(request):
    """ Add a review to the store """
    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
