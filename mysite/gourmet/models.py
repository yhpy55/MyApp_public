from django.db import models


class Gourmet(models.Model):
    name = models.CharField(max_length=100)
    station = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    holiday = models.CharField(max_length=30,null=True)
    wifi = models.CharField(max_length=10,null=True)
    non_smoking = models.CharField(max_length=10,null=True)
    urls = models.URLField(max_length=100,null=True)
    coupon_urls = models.URLField(max_length=100,null=True)
    shop_id = models.CharField(max_length=10,default=0)

    def __str__(self):
        return f'<Gourmet:id= {self.name} {self.station} {self.genre}>'
