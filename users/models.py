from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .validators import UsernameValidator
from logging import getLogger

logger = getLogger(__name__)


class UserManager(BaseUserManager):
    """
    ユーザーマネージャー
    """
    user_in_migrations = True

    def _create_user(self, email, password, username, **kwargs):
        if not email or email == '':
            raise ValueError('メールアドレスは必須です')
        if not password or password == '':
            raise ValueError('パスワードは必須です')
        if not username or username == '':
            raise ValueError('ユーザー名は必須です')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_joined=timezone.now()
        )
        user.set_password(password)
        try:
            user.save(using=self._db)
        except Exception as e:
            logger.exception(f'Exception at UserManager._create_user: {e}')
        return user

    # ユーザー登録
    def create_user(self, email, password, username, **kwargs):
        return self._create_user(email, password, username)

    # スーパーユーザー登録
    def create_superuser(self, email, password, username, **kwargs):
        user = self.create_user(email, password, username)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    ユーザーモデル
    """
    # Emailアドレス
    email = models.EmailField(_('email'), blank=True)
    # ユーザー名validator
    username_validator = UsernameValidator()
    # ユーザー名
    username = models.CharField(
        _('username'),
        max_length=50,
        validators=[username_validator],
        unique=True
    )
    display_username = models.CharField(
        _('disp_username'),
        max_length=50,
        blank=True
    )
    # プロフィール
    profile = models.CharField(_('profile'), blank=True, max_length=400)
    # アイコン画像
    icon_image = models.URLField(blank=True)
    # スタッフフラグ
    is_staff = models.BooleanField(
        _('is_staff'),
        default=False
    )
    # 論理削除フラグ
    is_active = models.BooleanField(
        _('is_active'),
        default=True
    )
    # 管理者フラグ
    is_admin = models.BooleanField(
        _('is_admin'),
        default=False
    )
    # スーパーユーザーフラグ
    is_superuser = models.BooleanField(
        _('is_superuser'),
        default=False
    )
    # 登録日時
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    # ユーザー名フィールド設定
    USERNAME_FIELD = 'username'
    # Eメールドレスフィールド設定
    EMAIL_FIELD = 'email'
    # 必須フィールド設定
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
