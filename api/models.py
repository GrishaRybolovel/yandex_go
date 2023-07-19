from django.db import models


class Price(models.Model):
    price = models.IntegerField()
    point_from_x = models.FloatField()
    point_from_y = models.FloatField()
    point_to_x = models.FloatField()
    point_to_y = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "price"