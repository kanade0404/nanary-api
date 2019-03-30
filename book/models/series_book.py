from django.db import models
from django.utils.translation import ugettext_lazy as _
from .series import Series
from .book import Book


class SeriesBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('book_title'))
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name=_('series_name'))

    class Meta:
        db_table = 'series_book'
        verbose_name = 'series and book'
