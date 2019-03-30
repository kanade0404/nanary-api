from django.db import models
from django.utils.translation import ugettext_lazy as _


class Provider(models.Model):
    """
    Provider Model
    """
    # Provider name
    provider_name = models.CharField(_('provider_name'), unique=True, max_length=20)

    class Meta:
        db_table = 'providers'
