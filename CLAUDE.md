# Bitcoin Price Prediction - Django Web Application

## Project Overview
Bitcoin 가격 예측 웹 애플리케이션. 실시간 가격 데이터를 수집하고 ML 모델로 예측값을 시각화한다.

## Tech Stack
- **Backend**: Django 4.2, Django REST Framework
- **ML**: scikit-learn, pandas, numpy (LSTM/ARIMA 예측 모델)
- **Data Source**: CoinGecko API (무료), Binance API
- **Frontend**: Bootstrap 5, Chart.js (가격 차트)
- **DB**: SQLite (개발), PostgreSQL (운영)
- **Task Queue**: Celery + Redis (주기적 데이터 수집)

## Project Structure
```
bitcoin_predict/          # Django 프로젝트 루트
├── config/               # 프로젝트 설정 (settings, urls, wsgi)
├── apps/
│   ├── market/           # 가격 데이터 수집 & 저장
│   ├── prediction/       # ML 예측 모델
│   └── dashboard/        # 프론트엔드 뷰
├── static/
├── templates/
├── requirements.txt
└── manage.py
```

## Key Features
1. **실시간 가격 대시보드** — Bitcoin 현재가, 24h 변동률
2. **가격 예측** — 다음 1h/24h/7d 예측 (ML 모델)
3. **히스토리 차트** — Chart.js로 OHLCV 시각화
4. **알림** — 목표가 도달 시 알림 (선택)

## Development Commands
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
celery -A config worker -l info        # 백그라운드 데이터 수집
```

## Code Conventions
- Django apps: `apps/` 하위에 위치
- API 뷰: DRF ViewSet 사용
- 모델 필드: snake_case
- 환경변수: `django-environ` 사용, `.env` 파일 (git 제외)
- 테스트: `pytest-django` 사용

## Agent Instructions
- 새 기능은 별도 앱으로 분리할 것
- 외부 API 호출은 `services.py`에 캡슐화
- ML 모델 학습/추론은 `prediction/` 앱 내에서만
- 민감 정보(API 키)는 `.env`에 보관, 절대 커밋 금지
- 마이그레이션 파일은 항상 커밋에 포함
