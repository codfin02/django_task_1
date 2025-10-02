# django_task_14

JWT 인증과 Swagger 문서가 포함된 레스토랑/리뷰 REST API 예제입니다. Day 13 코드를 확장해 설정 분리, Swagger 스키마, Simple JWT, 베이스 모델 등을 적용했습니다.

## 주요 기능
- 다중 설정: `config/settings/base|local|prod.py` 분리, `secret.json`에서 비밀키·DB 정보 로딩
- 인증: 커스텀 사용자 모델(`users.User`) + DRF Session 인증 + `djangorestframework-simplejwt` 설정 준비
- API 문서화: `drf-yasg` 기반 Swagger/Redoc 스키마(`config/schema.py`) 제공
- 도메인 모델: 레스토랑(`Restaurant`)과 리뷰(`Review`) CRUD + 공통 `BaseModel`로 created/updated 관리
- 테스트: User/Restaurant/Review 전용 `APITestCase`로 엔드포인트 동작 검증

## 개발 환경 준비
1. 가상환경 생성 및 활성화
   ```bash
   cd django_task_14
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. 필수 패키지 설치
   ```bash
   pip install django djangorestframework django-cleanup drf-yasg djangorestframework-simplejwt pillow
   ```
3. (선택) `secret.json` 작성 예시
   ```json
   {
     "DJANGO_SECRET_KEY": "your-secret-key",
     "DB": {
       "NAME": "db.sqlite3",
       "USER": "",
       "PASSWORD": "",
       "HOST": "",
       "PORT": ""
     }
   }
   ```
4. 마이그레이션 후 서버 실행
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## 주요 엔드포인트
- 사용자: `/users/login/`, `/users/signup/`, `/users/logout/`, `/users/profile/<int:pk>/`
- 레스토랑: `/restaurants/`, `/restaurants/<int:pk>/`
- 리뷰: `/restaurants/<int:restaurant_id>/reviews/`, `/reviews/<int:review_id>/`
- 문서화: `/swagger/`, `/redoc/`, `/swagger.json`, `/swagger.yaml`

## 테스트
```bash
python manage.py test
```
DRF APITestCase로 사용자 인증, 레스토랑 CRUD, 리뷰 CRUD가 모두 검증됩니다.

## 기타
- `STATICFILES_DIRS`에 맞춰 `static/` 디렉터리를 포함했습니다.
- `SIMPLE_JWT` 설정이 추가되어 있어 토큰 발급 뷰를 연결하면 바로 JWT 인증 흐름을 확장할 수 있습니다.
