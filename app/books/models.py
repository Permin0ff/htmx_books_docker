from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    author = models.CharField(verbose_name=_('Author'), max_length=200)
    price = models.PositiveIntegerField(verbose_name=_('Price'), default=0)
    read = models.BooleanField(verbose_name=_('Read'), default=False)

    def __str__(self):
        return self.title
