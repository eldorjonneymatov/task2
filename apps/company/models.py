from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import Profile


class Company(BaseModel):
    name = models.CharField(_("Name"), max_length=40)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name


class Product(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="products", verbose_name=_("Company"))
    name = models.CharField(_("Name"), max_length=100)
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=10)
    discount = models.PositiveSmallIntegerField(_("Discount"), default=0)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Review(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="reviews", verbose_name=_("Company"))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="reviews", verbose_name=_("Profile"))
    comment = models.TextField(_("Comment"), max_length=400)
    rating = models.PositiveSmallIntegerField(_("Rating"))
    is_active = models.BooleanField("Is active", default=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.comment
