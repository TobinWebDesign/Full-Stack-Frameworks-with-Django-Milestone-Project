from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_retreats, name='retreats'),
    path('<int:retreat_id>/', views.retreat_detail, name='retreat_detail'),
    path('add/', views.add_retreat, name='add_retreat'),
    path('edit/<int:retreat_id>/', views.edit_retreat, name='edit_retreat'),
]

