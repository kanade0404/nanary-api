import uuid
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from api.book.models.book import Book
from api.users.models import User


class Question(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('title'), max_length=100)
    content = models.TextField(_('content'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('book'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
    updated_at = models.DateTimeField(_('updated_at'), default=timezone.now)

    class Meta:
        db_table = 'questions'
        verbose_name = _('question')

    def __str__(self):
        return self.title
