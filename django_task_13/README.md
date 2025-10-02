# django_task_13

레스토랑/리뷰 서비스를 위한 Django REST Framework 기반 API 예제입니다. 커스텀 사용자 모델을 정의하고, DRF 제너릭 뷰/뷰셋을 활용해 사용자·레스토랑·리뷰 CRUD를 제공합니다.

## 주요 기능
- `AUTH_USER_MODEL` 교체: 이메일 기반 로그인(`users.User`)과 회원가입/프로필 수정/삭제 API 제공
- 레스토랑 API: `ModelViewSet` + DRF 라우터로 목록, 생성, 수정, 삭제를 한 클래스에 구현
- 리뷰 API: `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`로 레스토랑별 리뷰 관리
- TDD 샘플: User/Restaurant/Review 각각 `APITestCase`로 CRUD 시나리오 검증
- 공통 베이스 모델(`config.models.BaseModel`)로 생성/수정 시각 자동 관리

## 개발 환경 준비
1. 가상환경 생성 및 활성화 (예시는 venv)
   ```bash
   cd django_task_13
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. 필수 패키지 설치
   ```bash
   pip install django djangorestframework django-cleanup pillow
   ```
3. 마이그레이션 및 서버 실행
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## 주요 엔드포인트
- 사용자
  - `POST /users/signup/` : 회원가입
  - `POST /users/login/` : 세션 로그인
  - `POST /users/logout/` : 로그아웃
  - `GET/PATCH/DELETE /users/profile/<int:pk>/` : 본인 정보 조회·수정·삭제
- 레스토랑(라우터 기반)
  - `GET/POST /restaurants/`
  - `GET/PATCH/DELETE /restaurants/<int:pk>/`
- 리뷰
  - `GET/POST /restaurants/<int:restaurant_id>/reviews/`
  - `GET/PATCH/DELETE /reviews/<int:review_id>/`

## 테스트
다음 명령으로 API 테스트 케이스를 실행할 수 있습니다.
```bash
python manage.py test
```
테스트는 사용자 인증, 레스토랑 CRUD, 리뷰 CRUD 시나리오를 모두 검증합니다.

## 기타
- 미디어 파일 정리를 위해 `django-cleanup`을 등록했습니다.
- 비밀키/DB 정보는 `secret.json`에서 읽어오도록 구성되어 있으며 파일이 없으면 SQLite + 기본 비밀키로 동작합니다.
