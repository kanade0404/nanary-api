import re
from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[a-z0-9-]+$'
    message = (
        '正しいユーザー名を入力してください。ユーザー名は必須です。'
        '半角の小文字英字と数字、ハイフンが入力できます。'
    )
    flags = re.ASCII
