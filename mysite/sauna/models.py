from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return f'<Friend:id= {str(self.id)}, {self.name} ({str(self.age)})>'

class Sauna(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    fee = models.IntegerField(default=0)
    holiday = models.CharField(max_length=10)

    def __str__(self):
        return f'<Sauna:id= {self.name}, {self.address}, {str(self.fee)}, {str(self.holiday)}>'