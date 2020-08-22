from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Class
from django.contrib.auth.decorators import login_required
from .forms import ClassForm

# Create your views here.

def all_classes(request):
    """ A view to show all classes """

    classes = Class.objects.order_by('day', 'time')

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)

def class_detail(request, class_id):
    """ A view to show idividual classs """

    class_detail = get_object_or_404(Class, sku=class_id)

    context = {
        'class': class_detail,
    }
    
    return render(request, 'classes/class_detail.html', context)

def add_class(request):
    """ Add a yoga class to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            add_class = form.save()
            messages.success(request, 'Yey! Successfully added class!')
            return redirect(reverse('classes'))
        else:
            messages.error(request, 'Opps! Failed to add class. Please ensure the form is valid.')
    else:
        form = ClassForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)