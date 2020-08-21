from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('add_review/', views.add_review, name='add_review'),
]