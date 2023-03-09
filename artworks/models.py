from django.db import models


class Artist(models.Model):
    """
    Model for the artists selling artworks on the site.

    SKU Code should be a short string, preferably all caps.
    SKU Codes from Artist, Canvas, and Design are
    concatenated to render the Artwork SKU.
    """
    name = models.CharField(max_length=80)
    sku_code = models.CharField(
        max_length=6,
        verbose_name="SKU Code")
    friendly_name = models.CharField(
        max_length=80,
        verbose_name="Friendly Name")
    full_name = models.CharField(
        max_length=240,
        null=True,
        blank=True,
        verbose_name="Full Name")
    location = models.CharField(
        max_length=240,
        null=True,
        blank=True)
    description = models.TextField(
        null=True,
        blank=True)
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Image URL")
    image = models.ImageField(
        null=True,
        blank=True)
    banner_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Image URL")
    banner = models.ImageField(
        null=True,
        blank=True)
    facebook_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Facebook")
    twitter_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Twitter")
    insta_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Instagram")
    deviant_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="DeviantArt")
    pin_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Pinterest")
    etsy_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Etsy")

    def __str__(self):
        return self.name

    def get_sku_code(self):
        return self.sku_code

    def get_friendly_name(self):
        return self.friendly_name


class Canvas(models.Model):
    """
    Model for the types of product ("canvas") on which designs can be printed.

    SKU Code should be a short string, preferably all caps.
    SKU Codes from Artist, Canvas, and Design are
    concatenated to render the Artwork SKU.
    """
    name = models.CharField(max_length=80)
    sku_code = models.CharField(
        max_length=12,
        verbose_name="SKU Code")
    friendly_name = models.CharField(
        max_length=80,
        verbose_name="Friendly Name")
    description = models.TextField(null=True, blank=False)
    material = models.TextField(null=True, blank=False)
    dimensions = models.TextField(null=True, blank=False)
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Image URL")
    image = models.ImageField(
        null=True,
        blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Canvasses"

    def __str__(self):
        return self.name

    def get_sku_code(self):
        return self.sku_code

    def get_friendly_name(self):
        return self.friendly_name


class Design(models.Model):
    """
    Model for the designs that can be printed on various canvasses.

    SKU Code should be a short string, preferably all caps.
    SKU Codes from Artist, Canvas, and Design are
    concatenated to render the Artwork SKU.
    """
    name = models.CharField(max_length=80)
    sku_code = models.CharField(
        max_length=12,
        verbose_name="SKU Code")
    friendly_name = models.CharField(
        max_length=80,
        verbose_name="Friendly Name")
    description = models.TextField(null=True, blank=False)
    material = models.TextField(null=True, blank=False)
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Image URL")
    image = models.ImageField(
        null=True,
        blank=True)
    artist = models.ForeignKey(
        'Artist',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_sku_code(self):
        return self.sku_code

    def get_friendly_name(self):
        return self.friendly_name


class Artwork(models.Model):
    """
    Model for the individual products ("artworks") sold on the site.

    SKU is concatenated from Artist, Canvas, and Design.
    Some artwork info is stored in other models, e.g. Canvas and Design.
    This reduces duplication of info and allows centralised updates.
    For instance, the dimensions of each mug will always be the same.
    If the mug price changes, that is automatically applied to all mugs.
    """
    sku = models.CharField(
        max_length=40,
        verbose_name="SKU")
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(
        max_length=250,
        verbose_name="Friendly Name")
    artist = models.ForeignKey(
        'Artist',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    canvas = models.ForeignKey(
        'Canvas',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    design = models.ForeignKey(
        'Design',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Image URL")
    image = models.ImageField(
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
