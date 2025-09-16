# django_task_2

간단한 Todo 관리 기능을 제공하는 Django 프로젝트입니다. 할 일 목록을 확인하고, 각 항목의 상세 정보를 확인할 수 있는 두 개의 화면으로 구성됩니다.

## 구현 내용
- `Todo` 모델을 정의하여 제목, 설명, 시작일, 마감일, 완료 여부와 생성/수정 일시를 저장합니다.
- `/todo/` 경로에서 전체 할 일 목록을 조회할 수 있는 화면을 제공합니다.
- 목록에서 항목을 선택하면 `/todo/<id>/` 경로에서 상세 정보를 확인할 수 있습니다.
- 템플릿은 기본적인 스타일을 포함하여 웹 브라우저에서 바로 확인할 수 있습니다.

## 실행 방법
1. Python 3.12 이상과 [Poetry](https://python-poetry.org/)가 설치되어 있어야 합니다.
2. 프로젝트 루트에서 의존성을 설치합니다.
   ```bash
   poetry install
   ```
3. 데이터베이스 마이그레이션을 적용합니다.
   ```bash
   poetry run python manage.py migrate
   ```
4. 개발 서버를 실행합니다.
   ```bash
   poetry run python manage.py runserver
   ```
5. 브라우저에서 `http://127.0.0.1:8000/todo/` 로 접속해 할 일 목록을 확인합니다.

필요하다면 Django 관리자 사이트(`http://127.0.0.1:8000/admin/`)를 사용하기 위해 슈퍼유저를 생성하세요.
```bash
poetry run python manage.py createsuperuser
```
