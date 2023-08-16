from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    first_name = models.CharField(_("First name"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=30, null=True, blank=True)
    avatar = models.ImageField(_("Avatar"), upload_to="avatars/", default="default_avatar.png")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
