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
        (1, '5 Day Meditation in Morocco'),
        (2, '7 Day Authentic Yoga Retreat in Ireland'),
        (3, '5 Day Authentic Yoga in Italy'),
        (4, 'Surf & yoga in Ireland'),
        (5, 'Hatha Yoga'),
        (6, 'Yoga 4 Beginners'),
        (7, 'Ashtanga Yoga'),
        (8, 'Vinyasa yoga'),
        (9, 'Iyengar Yoga'),
    )
    product = models.IntegerField(choices=PRODUCT_CHOICES)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)