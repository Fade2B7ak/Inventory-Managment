from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=42, unique=True)
    personal_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default="Enter your password here")
    confirm_password = models.CharField(max_length=50, default="Confirm your password here")

    REQUIRED_FIELDS = ['username', 'email', 'password']
    USERNAME_FIELD = 'username'


class Inventory(models.Model):
    itemClass = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    price = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ], null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    ready_to_load = models.BooleanField(default=False)
    cost_per_piece = models.IntegerField(default=True)

    def __str__(self):
        return self.itemClass + ", " + self.name + ", " + self.model + ", " + str(self.quantity) + ", " +\
            str(self.cost_per_piece) + "€" + ", " + str(self.price) + "€" + ", " + str(self.stock_date)
