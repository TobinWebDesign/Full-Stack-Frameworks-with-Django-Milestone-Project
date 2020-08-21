from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.all_reviews, name='reviews'),
    url('add_review', views.add_reviews, name='add_reviews'),
]