# django_task_5

CBV(Class-Based Views)로 ToDo CRUD를 구현하고 URL include, 템플릿 수정, Admin 권한 로직을 반영한 예제입니다.

- URL prefix: `/cbv/`
- 목록/상세/생성/수정/삭제 모두 CBV(LoginRequiredMixin)로 구현
- Admin은 전체 사용자 Todo 조회/수정/삭제 가능, 목록에서 사용자명 표시

실행 방법
1) 가상환경 및 설치(저장소 루트의 venv 사용 가정)
```bash
cd django_task_5
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```
2) 주요 URL
- 목록: `/cbv/todo/` (검색 `?q=키워드`, 페이지 `?page=2`)
- 생성: `/cbv/todo/create/`
- 상세: `/cbv/todo/<pk>/`
- 수정: `/cbv/todo/<pk>/update/`
- 삭제: `/cbv/todo/<pk>/delete/`
