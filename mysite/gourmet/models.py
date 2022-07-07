from django.db import models

class MyList(models.Model):
    name = models.CharField(max_length=100)
    station = models.CharField(max_length=30)
    jenre = models.CharField(max_length=30)
    holiday = models.CharField(max_length=30)
    wifi = models.BooleanField()
    url = models.URLField()
    mail = models.EmailField(max_length=50)
    registdate = models.DateField()

    def __str__(self):
        return f'<MyList:id= {self.name} {self.station} {self.jenre} ({str(self.registdate)})>'