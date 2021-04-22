from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .products import *

User = get_user_model()

# Create your models here.


class LatestProductManager:

    @staticmethod
    def get_products_for_main_page(self, *args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in = args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model = with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key = lambda x: x.__class__._meta.model_name.startswith(with_respect_to),
                        reverse = True
                    )
        return products


class LatestProducts:
    objects = LatestProductManager


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name = 'Customer', on_delete = models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name = 'Cart', on_delete = models.CASCADE, related_name =
    'related_products')
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default = 1)
    final_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Total Price')

    def __str__(self):
        return "Product: {} (for Cart)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name = 'Owner', on_delete = models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank = True, related_name = 'related_cart')
    total_products = models.PositiveIntegerField(default = 0)
    final_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Total Price')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name = 'Customer', on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 20, verbose_name = 'Phone number')
    address = models.CharField(max_length = 255, verbose_name = 'Address')

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user.last_name)
