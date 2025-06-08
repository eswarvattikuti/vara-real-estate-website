from django.db import models
from django.utils.translation import gettext_lazy as _ # For choices

class Property(models.Model):
    STATUS_CHOICES = [
        ('FOR_SALE', _('For Sale')),
        ('SOLD', _('Sold')),
        ('PENDING', _('Pending')),
        ('DRAFT', _('Draft')),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2) # Suitable for currency like INR
    area_sqft = models.IntegerField(verbose_name=_('Area (sqft)'))
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    features = models.TextField(blank=True, help_text=_('Comma-separated values, e.g., Garden, Pool'))
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='DRAFT',
    )
    # For ImageField, Pillow needs to be installed. Image will be uploaded to MEDIA_ROOT / 'property_images/'
    main_image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
        ordering = ['-date_added']
