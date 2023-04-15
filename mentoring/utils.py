from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    """A class that represents posible genders"""
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")


PROJECT_STATUS_CHOICES = ((True, _('Active')), (False, _('Deleted')))
