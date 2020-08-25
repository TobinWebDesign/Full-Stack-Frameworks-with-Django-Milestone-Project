from django.db import models

# Create your models here.

class Level(models.Model):


    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

"""
   A timetable for yoga classes to be displayed to the customer
"""

class Class(models.Model):

    class Meta:
        verbose_name_plural = 'Classes'

    DAYS_OF_THE_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday')
    )

    YOGA_CLASS_TIMES = (
        ('1', '06:00'),
        ('2', '08:00'),
        ('3', '12:00'),
        ('4', '18:00'),
        ('5', '20:00')       
    )

    level = models.ForeignKey('Level', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dificulty = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    day = models.CharField(max_length=10, choices=DAYS_OF_THE_WEEK, null=True, blank=True)
    time = models.CharField(max_length=10, choices=YOGA_CLASS_TIMES, null=True, blank=True)

    def __str__(self):
        return self.name
