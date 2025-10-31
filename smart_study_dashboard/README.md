# Smart Study Dashboard

**Smart Study Dashboard**는 뽀모도로(Pomodoro) 방식으로 공부 시간을 기록/시각화하는 Python 데스크톱 앱입니다.  
Tkinter GUI + SQLite 저장소 + matplotlib 그래프를 사용합니다.

---

## Features
- Pomodoro 타이머 (Start / Pause / Reset)
- 로컬 SQLite에 세션 기록(날짜·초·작업·카테고리) 저장
- 주간 학습 그래프 시각화 (matplotlib) *(Roadmap)*
- CSV 내보내기 *(Roadmap)*
- UI 정돈 및 안정화 *(Roadmap)*

---

## Roadmap
- [x] 기본 UI 프레임 및 타이머
- [x] SQLite 연동 및 세션 저장
- [ ] 주간 그래프 시각화 (matplotlib)
- [ ] CSV Export
- [ ] UI/이벤트 안정화 및 최종 정리

> 상세 진행은 `dev-log.md` 참고.

---

## Tech Stack
- Python 3.11
- Tkinter, SQLite (sqlite3), matplotlib, pytest

---

## How to Run
``` bash

# (옵션) 가상환경 활성화 후
python study_dash/main.py

```
>앱 실행 시 Tkinter GUI가 열립니다.

---

## Project Structure
```

smart_study_dashboard/
 ├─ main.py            # 앱 엔트리 포인트 (UI 초기화 및 DB init 호출)
 ├─ timer.py           # PomodoroTimer 핵심 로직 (카운트다운 / 제어)
 ├─ ui.py              # 전체 Tkinter UI 프레임 구성 및 레이아웃 관리
 ├─ db_service.py      # SQLite 접근 모듈 (init_db, insert/fetch 등)
 ├─ data/              # (실행 시 자동 생성) study_data.db 저장 위치
 ├─ tests/             # 단위 테스트 디렉토리 (pytest 기반)
 │   ├─ test_timer_basic.py   # 타이머 기본 동작 테스트
 │   └─ test_db_service.py    # DB 연동 및 CRUD 테스트
 └─ dev-log.md         # 주차별 개발 기록 및 학습 로그
 
```

## Documentation
- 주차별 구현 내역과 학습 기록: dev-log.md

---

## Author
- 추명곤 (Bucheon Univ. 정보통신공학과)