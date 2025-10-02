# django_task_08

이 프로젝트는 이메일 인증 기반 사용자 가입 플로우를 다루는 Django 예제입니다. Day 7 Todo 앱을 확장해 회원가입 시 이메일 인증을 거친 뒤 로그인할 수 있도록 구성했습니다.

## 주요 기능
- 커스텀 User 모델과 매니저(`users.User`)로 이메일을 아이디로 사용
- 회원가입 시 인증 메일 발송/검증 플로우(`/users/signup/`, `/users/verify/`)
- 로그인/로그아웃/회원탈퇴를 포함한 기본 인증 기능
- Bootstrap 기반 템플릿과 정적 파일(`static/css/bootstrap.css`, `static/js/bootstrap.bundle.js`)

## 개발 환경 설정
1. 가상환경 생성 및 활성화
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. 패키지 설치
   ```bash
   pip install django
   ```
3. 데이터베이스 마이그레이션 및 서버 실행
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## 기본 URL
- 홈: `/`
- 회원가입: `/users/signup/`
- 인증 메일 재전송: `/users/signup/resend/`
- 로그인: `/users/login/`
- 인증 성공/실패 페이지: `/users/verify/success/`, `/users/verify/failed/`

## 테스트
본 예제에는 자동화 테스트가 포함되어 있지 않습니다. 회원가입 → 인증 → 로그인 시나리오를 실제로 실행해 확인해 주세요.
