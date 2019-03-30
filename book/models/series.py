from django.db import models
from django.utils.translation import ugettext_lazy as _


class Series(models.Model):
    name = models.CharField(_('series_name'), max_length=100)

    class Meta:
        db_table = 'series'
        verbose_name = _('series')

    def __str__(self):
        return self.name
