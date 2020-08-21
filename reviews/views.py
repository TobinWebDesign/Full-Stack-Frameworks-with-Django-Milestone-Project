from django.shortcuts import get_object_or_404, render

from .models import Review

def all_reviews(request):

    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
        }

    
    return render(request, 'reviews/reviews.html', context)

def add_review(request):
    """ Add a review to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Yey! Successfully added review!')
            return redirect(reverse('review_detail', args=[review.sku]))
        else:
            messages.error(request, 'Opps! Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)