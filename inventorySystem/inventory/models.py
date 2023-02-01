from django.db import models


class Inventory(models.Model):
    itemClass = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    ready_to_load = models.BooleanField(default=False)
    data_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.itemClass + ", " + self.name + ", " + self.model + ", " + str(self.quantity) + ", " +\
            str(self.price) +"€" + ", " + str(self.stock_date)

