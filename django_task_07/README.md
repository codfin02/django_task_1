# django_task_7

Summernote 기반 리치 텍스트 + 이미지 업로드(완료 이미지 + 썸네일)를 Todo에 적용한 예제입니다.

- 라이브러리: `django-summernote`, `pillow`, `django-cleanup`
- 설정: MEDIA/STATIC 경로, Summernote(iframe) 보안 설정, cleanup 등록
- 모델: `Todo.thumbnail`, `Todo.completed_image` + `save()` 오버라이드로 썸네일 생성
- 폼: SummernoteWidget 적용, 파일 입력(완료 이미지), Bootstrap 폼 제어
- 뷰: CBV(Create/Update는 폼 클래스 사용), 댓글 CRUD 포함
- URL: `/cbv/todo/…`, `/cbv/comment/…`, `/summernote/`

실행 방법
```bash
cd django_task_7
../.venv/bin/pip install django-summernote pillow django-cleanup
../.venv/bin/python manage.py makemigrations
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```

확인 경로
- 목록: `http://127.0.0.1:8000/cbv/todo/`
- 관리자: `/admin/` (Todo/Comment 관리, description에 Summernote 적용)

