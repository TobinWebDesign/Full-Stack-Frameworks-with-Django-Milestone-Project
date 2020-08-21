from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.all_reviews, name='reviews'),
]