from django.db import models
from django.utils.translation import ugettext_lazy as _


class Publisher(models.Model):
    name = models.CharField(_('publisher_name'), max_length=100)

    class Meta:
        db_table = 'publishers'
        verbose_name = _('publisher')

    def __str__(self):
        return self.name
