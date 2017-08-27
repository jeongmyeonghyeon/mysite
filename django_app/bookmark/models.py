# 파이썬 3 문법 문자열을 파이썬 2 문법 문자열로 자동변환 해주는 모듈
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# 파이썬 버전과 무관하게 하나의 메소드만 사용하게 하는 방식
@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title
