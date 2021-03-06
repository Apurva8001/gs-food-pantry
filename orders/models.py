from django.db import models
from shop.models import Product
from portfolio.models import Visit


class Order(models.Model):
    visit = models.ForeignKey(Visit, related_name='order', default=None, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Originally defaults to false but may want to switch to true because it is a food pantry (see page 236)
    paid = models.BooleanField(default=True)


class Meta:
    ordering = ('-created',)


def __str__(self):
    return 'Order {}'.format(self.id)


def created(self):
        self.created = timezone.now()
        self.save()


def updated(self):
    self.updated = timezone.now()
    self.save()


def get_total_cost(self):
    return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
