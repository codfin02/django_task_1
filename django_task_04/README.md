# django_task_4

ToDo CRUD + 검색(Q), 페이지네이션(Paginator), `login_required` 적용 예제입니다.

- 모델: `Todo.user`(FK)로 작성자 식별, 완료 여부 `is_completed`
- 폼: `TodoForm`, `TodoUpdateForm`(is_completed 포함)
- 뷰:
  - 목록 `todo_list`: 로그인 필수, 본인 데이터만, q 검색(Q), 페이지네이터로 `page_obj` 전달
  - 상세 `todo_info`: 로그인 필수, `get_object_or_404`, `todo.__dict`를 컨텍스트로 전달
  - 생성/수정/삭제: 로그인 필수, 생성 시 `form.save(commit=False)` → `todo.user = request.user`
- 템플릿: `templates/todo/{base,todo_list,todo_info,todo_create,todo_update}.html`

실행 방법
1) 가상환경 및 패키지
```bash
python -m venv .venv && source .venv/bin/activate
pip install "django>=5,<6"
```
2) 마이그레이션/서버
```bash
cd django_task_4
python manage.py migrate
python manage.py runserver
```
3) (선택) 관리자 계정
```bash
python manage.py createsuperuser
```

주요 URL
- 목록: `/todo/` (로그인 필수, 검색: `?q=키워드`, 페이지: `?page=2`)
- 생성: `/todo/create/`
- 상세: `/todo/<int:todo_id>/`
- 수정: `/todo/<int:todo_id>/update/`
- 삭제: `/todo/<int:todo_id>/delete/`
- 로그인/회원가입: `/accounts/login/`, `/accounts/signup/`
