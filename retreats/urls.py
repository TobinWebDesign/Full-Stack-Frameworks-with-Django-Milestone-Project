from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_retreats, name='retreats'),
    path('add/', views.add_retreat, name='add_retreat'),
    path('edit/<retreat_id>/', views.edit_retreat, name='edit_retreat'),
    path('delete/<retreat_id>/', views.delete_retreat, name='delete_retreat'),
    path('<retreat_id>/', views.retreat_detail, name='retreat_detail'),
]
