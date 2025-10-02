from django.conf import settings
from django.db import models


class Todo(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='todos',
        verbose_name='작성자',
    )
    title = models.CharField('제목', max_length=100)
    description = models.TextField('설명', blank=True)
    due_date = models.DateField('마감일', null=True, blank=True)
    is_completed = models.BooleanField('완료 여부', default=False)
    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    class Meta:
        verbose_name = '할 일'
        verbose_name_plural = '할 일 목록'
        ordering = ['is_completed', 'due_date', '-created_at']

    def __str__(self) -> str:
        return self.title

