from django.db import models

# Create your models here.
class Measurment(models.Model):

    DISTANCE_1 = models.FloatField(default=0)
    DISTANCE_2 = models.FloatField(default=0)
    PAD_THICKNESS_1 = models.FloatField(default=0)
    PAD_THICKNESS_2 = models.FloatField(default=0)
    DISTANCE_3 = models.FloatField(default=0)
    DISTANCE_4 = models.FloatField(default=0)




