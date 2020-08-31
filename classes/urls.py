from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_classes, name='classes'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<class_id>/', views.edit_class, name='edit_class'),
    path('edit/<class_id>/<type>', views.edit_class, name='edit_class'),
    path('delete/<class_id>/', views.delete_class, name='delete_class'),
    path('<class_id>/', views.class_detail, name='class_detail'),
 
]