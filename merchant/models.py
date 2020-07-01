from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

USER_TYPE_CHOICES = (
    ("A", "Client"),
    ("B", "Costumer")
)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    company = models.CharField(max_length=64, blank=True, null=True)
    address = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.username

class CostumerUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    costumer_phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Item(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("merchant:item-detail", kwargs={
            'slug': self.slug,
        })

    def get_add_to_order_url(self):
        return reverse("merchant:add-to-order", kwargs={
            'slug': self.slug,
        })

    def get_remove_item_from_cart_url(self):
        return reverse("merchant:remove-from-cart", kwargs={
            'slug': self.slug,
        })

class OrderItem(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    costumer = models.ForeignKey(CostumerUserProfile, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    costumer = models.ForeignKey(CostumerUserProfile, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    slug = models.SlugField()


    def __str__(self):
        return self.user_profile.user.username

    def save(self, *args, **kwargs):
        string = "%s %s" % (self.costumer.user.username, self.start_date)
        self.slug = slugify(string)
        super(Order, self).save()

    # def confirm_costumer_url(self):
    #     return reverse()

class ActiveOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    date_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.user.username} has activated this order"


