import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Series(models.Model):
    """
    Series Model
    """
    uuid = models.UUIDField(_('uuid'), db_index=True, default=uuid.uuid4, editable=False)
    # Series name
    name = models.CharField(_('series_name'), max_length=100)

    class Meta:
        db_table = 'series'
        verbose_name = _('series')

    def __str__(self):
        return self.name
