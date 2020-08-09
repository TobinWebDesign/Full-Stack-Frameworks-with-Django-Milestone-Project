from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_retreats, name='retreats'),
    path('<retreat_id>', views.retreat_detail, name='retreat_detail')
]
