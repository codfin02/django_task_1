from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('description', models.TextField(verbose_name='설명')),
                ('start_date', models.DateField(verbose_name='시작일')),
                ('end_date', models.DateField(verbose_name='마감일')),
                ('is_completed', models.BooleanField(default=False, verbose_name='완료 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
            ],
            options={
                'verbose_name': '할 일',
                'verbose_name_plural': '할 일 목록',
            },
        ),
    ]
