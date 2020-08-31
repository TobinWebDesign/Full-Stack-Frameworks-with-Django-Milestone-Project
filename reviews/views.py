from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def all_reviews(request):

    """ A view to show all reviews """
        #to display reviews by latest review
    reviews = Review.objects.order_by('-date') 

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

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review()
            review = form.save()
            messages.success(request, 'Yey! Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Opps! Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
