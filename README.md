# AI 챗봇

Django 기반의 AI 챗봇 애플리케이션입니다. Google Gemini AI 모델을 사용하여 자연스러운 대화를 제공합니다.

## 🚀 기능

- 🤖 Google Gemini 1.5 Flash 모델을 사용한 AI 챗봇
- 💬 실시간 채팅 인터페이스
- 🎨 모던하고 반응형 UI
- ⚡ 빠른 응답 속도
- 🌐 한국어 지원
- 🔍 실시간 로깅 및 에러 처리
- 🏥 헬스 체크 엔드포인트

## 📁 프로젝트 구조

```
ai_chatbot/
├── chatbot/                 # Django 앱 (실제 기능 구현)
│   ├── models.py           # 데이터베이스 모델
│   ├── views.py            # 뷰 로직 (챗봇 API 포함)
│   ├── urls.py             # 앱 레벨 URL 라우팅
│   ├── templates/          # HTML 템플릿
│   └── admin.py            # 관리자 페이지 설정
├── chatbot_project/        # Django 프로젝트 설정
│   ├── settings.py         # 프로젝트 설정
│   ├── urls.py             # 메인 URL 라우팅
│   └── wsgi.py             # WSGI 설정
├── requirements.txt        # Python 의존성
└── manage.py              # Django 관리 명령어
```

## 🛠️ 설치 및 실행

### 1. 저장소 클론
```bash
git clone <repository-url>
cd ai_chatbot
```

### 2. 가상환경 활성화
```bash
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 Google Gemini API 키를 설정하세요:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 6. 서버 실행
```bash
python manage.py runserver
```

### 7. 브라우저에서 접속
http://localhost:8000 으로 접속하여 챗봇을 사용하세요.

## 🔌 API 엔드포인트

- `GET /` - 챗봇 홈페이지
- `POST /api/chat/` - 챗봇 API (JSON 요청/응답)
- `GET /health/` - 헬스 체크 (API 키 상태 포함)

### 챗봇 API 사용 예시
```bash
curl -X POST http://localhost:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "안녕하세요!"}'
```

## 💻 사용법

1. 브라우저에서 http://localhost:8000 접속
2. 하단 입력창에 메시지 입력
3. Enter 키 또는 전송 버튼 클릭
4. AI 챗봇의 응답 확인

## 🛠️ 기술 스택

- **Backend**: Django 4.2.7
- **AI Model**: Google Gemini 1.5 Flash
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (기본)
- **Environment**: python-dotenv
- **HTTP Client**: requests

## ⚠️ 주의사항

- Google Gemini API 키가 필요합니다
- 인터넷 연결이 필요합니다
- API 사용량에 따라 비용이 발생할 수 있습니다
- `.env` 파일은 `.gitignore`에 추가하여 API 키가 노출되지 않도록 주의하세요

## 🔧 개발 환경 설정

### 로깅 설정
애플리케이션은 자동으로 로깅을 수행합니다:
- 사용자 메시지 수신 로그
- AI 응답 생성 완료 로그
- API 오류 로그

### 디버깅
헬스 체크 엔드포인트를 통해 API 키 설정 상태를 확인할 수 있습니다:
```bash
curl http://localhost:8000/health/
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
