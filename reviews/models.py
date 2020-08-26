from django.db import models

import numpy as np


class Product(models.Model):
    name = models.CharField(max_length=200)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    PRODUCT_CHOICES = (
        ('5 Day Meditation in Morocco', '5 Day Meditation in Morocco'),
        ('7 Day Authentic Yoga Retreat in Ireland', '7 Day Authentic Yoga Retreat in Ireland'),
        ('5 Day Authentic Yoga in Italy', '5 Day Authentic Yoga in Italy'),
        ('Surf & yoga in Ireland', 'Surf & yoga in Ireland'),
        ('Hatha Yoga', 'Hatha Yoga'),
        ('Yoga 4 Beginners', 'Yoga 4 Beginners'),
        ('Ashtanga Yoga', 'Ashtanga Yoga'),
        ('Vinyasa yoga', 'Vinyasa yoga'),
        ('Iyengar Yoga', 'Iyengar Yoga'),
    )
    product = models.CharField(max_length=200, choices=PRODUCT_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)