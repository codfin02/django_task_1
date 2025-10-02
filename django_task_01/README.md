# django_task_1

이 워크스페이스엔 Day 1 과제에 해당하는 장고 프로젝트 뼈대와 예제 뷰/템플릿이 포함되어 있습니다.

## 포함 내용
- Django 프로젝트 스캐폴딩(`manage.py`, `config/`)
- URL + View 예제: index, book_list, book detail, language
- 가짜 DB 예제: movies, movie_detail
- Template 예제: `templates/` 폴더와 HTML 파일들
- 미니프로젝트: 구구단 페이지 `gugu/<int:num>/`
- 기본 `.gitignore`

## 실행 방법
아래 중 하나를 선택하세요.

### A. pyenv + Poetry (권장)
1) pyenv/virtualenv 설치 후 가상환경 생성
```bash
pyenv install 3.12.1
pyenv virtualenv 3.12.1 oz
pyenv local oz
```
2) Poetry 설치 및 초기화(이미 pyproject가 없다면)
```bash
brew install poetry   # macOS
poetry init           # 질문은 기본값 사용해도 무방
```
3) 현재 가상환경을 Poetry 인터프리터로 지정
```bash
poetry env use $(pyenv which python)
```
4) Django 설치
```bash
poetry add django
```
5) 개발 서버 실행
```bash
python manage.py runserver
```

### B. venv + pip (간단)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django
python manage.py runserver
```

## 확인 URL
- 기본 페이지: http://127.0.0.1:8000/
- 책 목록: http://127.0.0.1:8000/book_list/
- 책 상세: http://127.0.0.1:8000/book_list/3/
- 언어 페이지: http://127.0.0.1:8000/language/Python/
- 영화 목록(가짜 DB): http://127.0.0.1:8000/movie/
- 영화 상세(가짜 DB): http://127.0.0.1:8000/movie/0/
- 구구단: http://127.0.0.1:8000/gugu/7/

## 비밀값 관리
- 민감정보는 `.env` 혹은 `secret.json`에 보관하고, `.gitignore`에 포함했습니다.
- Day 1 예제는 별도 비밀 키 로딩 없이 동작하지만, 실제 서비스에서는 환경변수 사용을 권장합니다.

## 참고
- 템플릿 경로는 `config/settings.py`에서 `BASE_DIR / 'templates'`로 설정되어 있습니다.
- 강의 흐름을 따라 초기에 `urls.py`에 간단한 뷰를 함께 작성했습니다. 실제 프로젝트에선 앱(`startapp`)으로 분리하는 방식을 권장합니다.
