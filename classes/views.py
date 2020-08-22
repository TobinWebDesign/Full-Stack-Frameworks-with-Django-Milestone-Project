from django.shortcuts import render, get_object_or_404
from .models import Class
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
    
    form = ClassForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)