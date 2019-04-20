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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name=_('publisher name'))
    # author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author name'))
    # book image
    cover = models.FileField(_('cover'), blank=True, max_length=255, upload_to='images/books/covers')
    # publish date(format:yyyyMM)
    publish_date = models.PositiveIntegerField(_('publish_date'), null=True)

    class Meta:
        db_table = 'books'
        verbose_name = _('book')

    def __str__(self):
        return self.title
