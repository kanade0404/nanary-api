from django.db import models
from django.utils.translation import ugettext_lazy as _
from category.models import Category


class Subject(models.Model):
    """
    Detail subject
    """
    # Major name
    name = models.CharField(_('subject_name'), unique=True, max_length=50)
    # Category number
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category_name'))

    class Meta:
        db_table = 'subjects'
        verbose_name = _('subject')

    def __str__(self):
        return self.name


class SubjectTag(models.Model):
    name = models.CharField(_('subject_tag_name'), max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject_name'))

    class Meta:
        db_table = 'subject_tags'
        verbose_name = _('subject tag')

    def __str__(self):
        return self.name
