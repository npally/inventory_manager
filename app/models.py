from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    product_id = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ['-quantity']

    def get_price(self):
        return "$" + format(self.price, ',.2f')

    def inventory_value(self):
        value= self.price * self.quantity
        return "$" + format(value, ',.2f')

    def add_inventory(self, qty, price):
        self.price = ((self.price * self.quantity) + (qty * price)) / (self.quantity + qty)
        self.quantity = self.quantity + qty

        self.save(update_fields=['price', 'quantity'])

    def remove_inventory(self, qty):
        self.quantity = self.quantity - qty

        self.save(update_fields=['quantity'])
