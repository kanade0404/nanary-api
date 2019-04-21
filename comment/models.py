import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from question.models import Question
from users.models import User


class Comment(models.Model):
    uuid = models.UUIDField(_('uuid'), db_index=True, default=uuid.uuid4, editable=False)
    content = models.TextField(_('content'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('question'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')

    def __str__(self):
        return self.content
