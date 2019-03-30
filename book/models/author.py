from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    """
    Author Model
    """
    # Author name
    name = models.CharField(_('author_name'), max_length=100)

    class Meta:
        db_table = 'authors'
        verbose_name = _('author')

    def __str__(self):
        return self.name
