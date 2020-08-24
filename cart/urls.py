from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('add/<item_id>/<type>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item>/', views.adjust_cart, name='adjust_cart'), # item allows redirect of either retreat+id or class+id
    path('remove/<item>/', views.remove_from_cart, name='remove_from_cart'),
]