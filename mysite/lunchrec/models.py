from django.db import models

class LunchrecList(models.Model):
    date = models.DateField()
    shop_name = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    remarks = models.CharField(max_length=100)

    def __str__(self):
        return f'<MyList:date= {str(self.date)}, {self.shop_name} {self.menu_name})>'