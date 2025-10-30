# Smart Study Dashboard

**Smart Study Dashboard**는 뽀모도로(Pomodoro) 방식을 기반으로 공부 시간을 체계적으로 관리하고 기록하는 **Python 데스크톱 애플리케이션**입니다.  
단순한 타이머를 넘어서, 학습 루틴을 시각적으로 확인하고 집중과 휴식을 효율적으로 설계할 수 있도록 돕습니다.

---

## 프로젝트 개요
| 구분 | 내용 |
|------|------|
| **프로젝트명** | Smart Study Dashboard |
| **개발 기간** | 2025년 10월 ~ 12월 |
| **개발 목적** | 공부 습관 개선 및 집중도 향상을 위한 타이머형 학습 도우미 |
| **개발 환경** | Python 3.11, Tkinter GUI, SQLite, matplotlib |
| **진행 형태** | 개인 프로젝트 (정보통신 프로젝트 과목) |

---

## 현재 구현된 기능 (W1 완료)
### 기본 UI 프레임 구축
- Tkinter 기반 메인 윈도우 구성  
- 타이머 영역과 상태 표시 라벨 분리  
- 버튼 레이아웃 (Start / Pause / Reset) 배치  

### Pomodoro 타이머 기능
- 기본 25분 세션 카운트다운  
- `after(1000)`을 이용한 1초 단위 UI 갱신  
- 일시정지(Pause) / 리셋(Reset) 기능 구현  
- 종료 시 “Time’s up!” 문구 표시  

### 테스트 코드 작성
- `test_timer_basic.py` 작성  
  - `time_left` 초기값 검증  
  - `is_running` 초기 상태 검증  

---

## 앞으로의 개발 계획
| 주차 | 목표 내용 |
|------|------------|
| **W2** | SQLite 연동 및 학습 세션 저장 기능 구현 |
| **W3** | matplotlib 기반 주간 학습 그래프 시각화 |
| **W4** | UI 정돈 및 이벤트 안정화 (after 콜백 개선) |
| **W5** | CSV 내보내기, 세션 카테고리 확장 |
| **W6** | 자동 스크린샷 및 최종 README 완성 |

---

## 기술적 포인트
- **Tkinter after()**를 이용한 비동기 타이머 구현  
- **is_running 플래그**로 중복 타이머 실행 방지  
- **객체지향 구조화**: `StudyDashUI` / `PomodoroTimer` 분리  
- **테스트 코드 기반 초기 상태 검증**  
- 추후 **SQLite 연동 + matplotlib 시각화**로 확장 예정  

---

## 📸 UI 예시 (예정)
> (스크린샷은 W2~W3 기능 구현 후 추가 예정)

| 메인 화면 예시 | 타이머 동작 예시 |
|:---------------:|:----------------:|
| ![UI 기본 프레임](https://via.placeholder.com/320x200?text=UI+Frame) | ![타이머 동작](https://via.placeholder.com/320x200?text=Timer+Running) |

---

## 실행 방법
``` bash

# 가상환경 활성화 후
python study_dash/main.py

```
>실행 시 Tkinter GUI 창이 열리며 “Start / Pause / Reset” 버튼으로 타이머를 제어할 수 있습니다.

---

## 디렉토리 구조
```

smart_study_dashboard/
 ├── study_dash/
 │    ├── main.py
 │    ├── ui.py
 │    ├── timer.py
 │    └── __init__.py
 ├── tests/
 │    └── test_timer_basic.py
 ├── dev-log.md
 └── README.md

```

---

## 개발 로그

상세한 주차별 구현 내역과 학습 내용은 dev-log.md 에 기록되어 있습니다.

---

## 개발자

| 이름 | 역할 | 학과 |
|------|------|------|
| 추명곤 | 프로젝트 설계 및 개발 | 부천대학교 정보통신공학과 |

---

>Smart Study Dashboard는 “스마트한 학습 루틴”을 만드는 첫 걸음입니다.
>추후 SQLite 기반 데이터 저장과 주간 그래프 통계를 통해 사용자의 학습 패턴을 시각화할 예정입니다.