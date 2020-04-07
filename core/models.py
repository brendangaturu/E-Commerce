from django.db import models
from django.conf import settings


class Item(Models.model):
    title = models.CharField(max_length=100)
    price = models.FloatField

    def __str__(self):
        return self.title

class OrderItem(Models.model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Order(Models.model):
#TODO: to add the AUTH_USER_MODEL
#    user = models.ForeignKey()
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title





