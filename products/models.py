from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s profile - Points: {self.total_points}"

    def add_points(self, points):
        self.total_points += points
        self.save()


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=64, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.barcode})" if self.barcode else self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class UserPoints(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='points')
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Points: {self.total_points}"

    class Meta:
        verbose_name = 'user point'
        verbose_name_plural = 'user points'

    def add_points(self, points):
        self.total_points += points
        self.save()


class PriceEntry(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_entries')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='price_entries')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )
    date_reported = models.DateField(default=timezone.now)
    reported_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reported_prices'
    )

    def __str__(self):
        return f"{self.product.name} at {self.store.name} - ${self.price} on {self.date_reported}"

    class Meta:
        ordering = ['-date_reported', 'store', 'product']
        verbose_name = 'price entry'
        verbose_name_plural = 'price entries'


@receiver(post_save, sender=PriceEntry)
def update_user_points(sender, instance, created, **kwargs):
    if created and instance.reported_by:
        points_awarded = 10  # Define how many points to award for a new price entry
        UserPoints.objects.get_or_create(user=instance.reported_by)[0].add_points(points_awarded)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=PriceEntry)
def update_user_points(sender, instance, created, **kwargs):
    if created and instance.reported_by:
        points_awarded = 10  # Define how many points to award for a new price entry
        profile, _ = UserProfile.objects.get_or_create(user=instance.reported_by)
        profile.add_points(points_awarded)
