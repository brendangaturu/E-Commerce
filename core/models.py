from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('SW','Sport are'),
    ('S', 'Shirt'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('','primary'),
    ('', 'secondary'),
    ('', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    cartegory = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title





