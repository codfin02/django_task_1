# django_task_6

Todo에 댓글(Comment) 기능을 CBV로 구현하고, Bootstrap5 정적 파일을 적용한 예제입니다.

- 정적 파일: `STATICFILES_DIRS` 설정, `static/css/bootstrap.css`, `static/js/bootstrap.bundle.js`
- 모델: `Todo`, `Comment(todo, user, message, created_at, updated_at)`
- 폼: `CommentForm`(Textarea rows/cols/class/placeholder)
- Admin: Todo 인라인으로 Comment 관리 + Comment 전용 Admin
- 뷰(CBV)
  - 목록: 로그인 필수, admin=전체/일반=본인, 검색(Q), 페이지네이션
  - 상세: prefetch_related로 댓글 최적화, 댓글 page_obj + CommentForm 컨텍스트 제공
  - 생성/수정/삭제: Todo, Comment 각각 권한 검사(작성자/관리자 외 404), 성공 시 상세로 이동
- URL(include)
  - `/cbv/todo/`, `/cbv/todo/create/`, `/cbv/todo/<pk>/`, `/cbv/todo/<pk>/update/`, `/cbv/todo/<pk>/delete/`
  - `/cbv/comment/<todo_id>/create/`, `/cbv/comment/<pk>/update/`, `/cbv/comment/<pk>/delete/`

실행 방법
1) 가상환경 사용(루트 venv 가정)
```bash
cd django_task_6
../.venv/bin/python manage.py makemigrations
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```
2) 접속/기능
- 목록: `http://127.0.0.1:8000/cbv/todo/`
- 댓글 작성/수정/삭제: 상세에서 폼 제출 또는 버튼으로 동작
- 관리자: `/admin/`에서 Todo/Comment 확인 및 관리

