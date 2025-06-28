# AI 챗봇

Django 기반의 AI 챗봇 애플리케이션입니다.

## 기능

- 🤖 OpenAI GPT-3.5-turbo 모델을 사용한 AI 챗봇
- 💬 실시간 채팅 인터페이스
- 🎨 모던하고 반응형 UI
- ⚡ 빠른 응답 속도
- 🌐 한국어 지원

## 설치 및 실행

### 1. 가상환경 활성화
```bash
source venv/bin/activate
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 OpenAI API 키를 설정하세요:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 5. 서버 실행
```bash
python manage.py runserver
```

### 6. 브라우저에서 접속
http://localhost:8000 으로 접속하여 챗봇을 사용하세요.

## API 엔드포인트

- `GET /` - 챗봇 홈페이지
- `POST /api/chat/` - 챗봇 API
- `GET /health/` - 헬스 체크

## 사용법

1. 브라우저에서 http://localhost:8000 접속
2. 하단 입력창에 메시지 입력
3. Enter 키 또는 전송 버튼 클릭
4. AI 챗봇의 응답 확인

## 기술 스택

- **Backend**: Django 4.2.7
- **AI Model**: OpenAI GPT-3.5-turbo
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (기본)

## 주의사항

- OpenAI API 키가 필요합니다
- 인터넷 연결이 필요합니다
- API 사용량에 따라 비용이 발생할 수 있습니다
