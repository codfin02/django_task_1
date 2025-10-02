# django_task_3

블로그 + 쿠키/세션 + 로그인/회원가입 + ToDo 보호 라우트를 포함한 Django 예제입니다.

- 블로그: 목록/상세, 쿠키 `visits` 증가, 세션 방문 카운트 표시
- 인증: Django Authentication 사용(로그인/로그아웃/회원가입), `LOGIN_REDIRECT_URL=/todo/`
- ToDo: 로그인한 사용자만 접근 가능 목록/상세(view에 `login_required` 적용)
- 템플릿: `templates/` 경로 사용

실행 방법
1) 가상환경 및 패키지
```bash
python -m venv .venv && source .venv/bin/activate
pip install "django>=5,<6"
```
2) 마이그레이션/서버
```bash
cd django_task_3
python manage.py migrate
python manage.py runserver
```
3) (선택) 관리자 계정
```bash
python manage.py createsuperuser
```

주요 URL
- 블로그 목록: `/`
- 블로그 상세: `/<int:pk>/`
- 로그인: `/accounts/login/`, 회원가입: `/accounts/signup/`
- ToDo 목록: `/todo/` (로그인 필요)
