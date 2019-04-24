import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    カテゴリーモデル
    大分類を扱うモデル
    (ex: 工学、物理学、経済学、etc...)
    """
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('category_name'), max_length=50, unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')

    def __str__(self):
        return self.name


class CategoryTag(models.Model):
    """
    カテゴリータグモデル
    カテゴリーモデルに紐付けるタグ
    """
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('category_tag_name'), max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))

    class Meta:
        db_table = 'category_tags'
        verbose_name = _('category tag')

    def __str__(self):
        return self.name
