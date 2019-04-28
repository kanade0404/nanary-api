import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .publisher import Publisher
from .author import Author


class Book(models.Model):
    """
    Book Model
    """
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    # book title
    title = models.CharField(_('book_title'), max_length=200)
    # ISBN Code(length is 10 or 13)
    isbn = models.CharField(_('isbn'), unique=True, max_length=13)
    # publisher
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name=_('publisher'))
    # author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author'))
    # book image
    cover = models.ImageField(_('cover'), blank=True, upload_to='cover')
    # publish date(format:yyyy-MM)
    publish_date = models.CharField(_('publish_date'), blank=True, max_length=7, default='')

    class Meta:
        db_table = 'books'
        verbose_name = _('book')

    def __str__(self):
        return self.title
