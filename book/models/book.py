from django.db import models
from django.utils.translation import ugettext_lazy as _
from .publisher import Publisher
from .author import Author


class Book(models.Model):
    title = models.CharField(_('book_title'), max_length=200)
    """
    ISBN
    10桁と13桁がある
    """
    isbn = models.CharField(_('isbn'), unique=True, max_length=13)
    """
    出版元
    """
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name=_('publisher name'))
    """
    著者
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author name'))
    """
    書影
    """
    cover = models.FileField(_('cover'), blank=True, max_length=255, upload_to='images/books/covers')
    """
    出版年月
    yyyyMMの符号なし整数
    """
    publish_date = models.IntegerField(_('publish_date'), null=True)

    class Meta:
        db_table = 'books'
        verbose_name = _('book')

    def __str__(self):
        return self.title
