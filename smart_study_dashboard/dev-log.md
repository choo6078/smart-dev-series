# Smart Study Dashboard – 개발 로그

## W1 진행 로그 (2025-10-21)

### 구현 개요
- Tkinter 기반 **Smart Study Dashboard**의 기본 UI 프레임 구축  
- **Pomodoro 타이머 기능** 구현 (25분 기본 세션, Start / Pause / Reset 기능)  
- 메인 윈도우, 타이머 영역, 상태 표시 라벨 구성  
- Python 3.11 환경에서 실행 및 테스트 진행  

---

### 주요 구현 내용
- `StudyDashUI` 클래스 설계  
  - Tkinter 윈도우 생성 및 타이머 프레임 구성  
  - 상태 라벨 추가 및 Pack 배치 구조 적용  
- `PomodoroTimer` 클래스 구현  
  - `after(1000)`을 통한 1초 단위 카운트다운  
  - `is_running` 플래그로 중복 실행 방지  
  - Pause/Reset 기능으로 타이머 제어  
- `tests/test_timer_basic.py` 작성  
  - `time_left`, `is_running` 초기 상태 검증  
  - Tkinter 루트 생성 및 파괴 흐름 이해  

---

### 학습 및 성장 과정

- **테스트의 의미 이해**  
  - 처음엔 단순 실행 확인용이라고 생각했지만,  
    `test_timer_basic.py`를 통해 “초기 상태 보장” 역할을 명확히 배움.  
  - 이걸 통해 *‘테스트 = 코드 신뢰성을 높이는 장치’* 라는 개념이 자리 잡음.  

- **`self` 개념 완전히 이해**  
  - 클래스 내부에서 `self`가 “객체 자신”을 가리킨다는 걸 코드 분석으로 체감함.  
  - `PomodoroTimer` 여러 개를 생성했을 때 각 인스턴스가 독립적으로 동작하는 이유도  
    `self` 덕분이라는 걸 깨달음.  

- **Git의 작동 원리 학습**  
  - `git add`, `commit`, `push` 순서가 단순 명령이 아니라  
    ‘변경 추적 → 기록 확정 → 원격 반영’이라는 단계를 이해함.  
  - 빨간색(modified), 초록색(staged) 상태의 차이도 직접 확인하며 정리함.  

- **Markdown 문법과 README 렌더링 구조 익힘**  
  - 코드블록(````bash`)과 디렉토리 트리(``` ... ```)를 직접 테스트하면서  
    GitHub 렌더링 규칙과 미리보기 방식(`Ctrl + Shift + V`)을 익힘.  
  - Markdown 작성도 단순히 꾸미는 게 아니라,  
    “개발자의 문서화 능력”을 보여주는 포트폴리오 요소라는 걸 깨달음.  

- **커밋 단위의 중요성 인식**  
  - 자잘한 수정마다 커밋을 남기면 로그가 지저분해지는 걸 경험함.  
  - 코드 단위(`feat`, `fix`)와 문서 단위(`docs`) 커밋을 분리하는 방식으로 정리함.  
  - 필요 시 `reset --soft`, `orphan branch`로 커밋 히스토리를 초기화하는 법까지 배움.  

---

### 기술적 인사이트
- `after()` 기반 비동기 UI 업데이트 구조 이해  
- `is_running` 플래그를 활용한 상태 관리  
- UI와 로직을 분리한 객체지향적 설계 구조  
- `after_cancel()`을 통한 안정적인 일시정지 처리  
- 테스트 코드의 역할과 Git 워크플로우 습득  

---

### 다음 목표 (W2)
- SQLite 연동 및 학습 세션 저장 기능 구현  
- 세션 시작/종료/지속시간 기록 및 DB 관리 구조 설계

## W2 진행 로그 (2025-10-31)

### 구현 개요
- **SQLite 연동 및 학습 세션 저장 기능 구현 (DB 연동 완료)**
- 타이머 종료 시 세션 데이터를 자동으로 **DB에 기록**하도록 연결
- DB 접근 전용 모듈(`db_service.py`) 분리로 **데이터 관리 책임 분리**
- `pytest`를 통한 CRUD 및 주간 합계(`fetch_daily_totals`) 검증 완료

---

### 주요 구현 내용
- **`db_service.py` 모듈 신규 작성**
  - `init_db()` : `data/study_data.db` 자동 생성 및 `sessions` 테이블 구조 정의
  - `insert_session()` : 세션 1건 저장 (날짜, 공부시간, 작업명, 카테고리)
  - `fetch_sessions()` : 날짜 조건 기반 세션 목록 조회
  - `fetch_daily_totals()` : 주간 그래프용 일자별 공부 시간 합계 반환
  - `row_factory` 설정으로 결과를 **딕셔너리처럼 컬럼명 접근 가능**하게 구성
- **`PomodoroTimer` 클래스 수정**
  - 타이머 종료(`Time’s up!`) 시 DB 자동 저장 로직 추가
  - `session_duration` 속성 도입 → 남은 시간이 아닌 **실제 세션 시간(초)** 저장
  - DB 연동 시 예외 발생 방지용 try/except 구조 적용 (선택적으로 반영 가능)
- **테스트 코드 강화 (`tests/test_db_service.py`)**
  - 임시 디렉토리(`tmp_path`)에 테스트 DB 생성해 프로덕션 DB 오염 방지
  - CRUD + 주간 집계 로직 단위 테스트 통과
  - `ModuleNotFoundError: db_service` → 상대 임포트(`from .db_service import ...`)로 해결

---

### 학습 및 성장 과정
- **SQLite 구조와 연결 원리 완전 이해**
  - `_connect()` = “DB 문 열고 들어간 상태”, `commit()` = “변경을 실제 파일에 반영”
  - `with _connect() as conn:` 구문이 자동으로 문을 닫아준다는 점을 배움
  - `conn.row_factory = sqlite3.Row`로 Row 객체를 컬럼명 기반으로 접근 가능하게 만드는 원리 숙지
- **SQL 테이블 정의 문법 이해**
  - `CREATE TABLE IF NOT EXISTS sessions (...)` 구문 분석을 통해 `id`, `date`, `duration_sec`, `task`, `category` 컬럼 구조를 정확히 파악
  - `INTEGER PRIMARY KEY AUTOINCREMENT`의 자동 증가 원리까지 이해함
- **조건 쿼리(query, conds, params)의 동작 구조 파악**
  - SQL 문자열을 유연하게 조립(`SELECT * FROM sessions WHERE ...`)하는 방식 이해
  - `params`를 사용해 안전한 쿼리 실행(SQL Injection 방지)을 학습
- **DB 트랜잭션 및 커넥션의 생명주기 이해**
  - 커넥트를 반환(return)하면 열린 연결이 유지되지만, `with` 블록은 자동으로 닫힘을 체감
  - “DB 문을 열고 들어가서 작업 후 닫는다”는 개념으로 정리

---

### 기술적 인사이트
- **Tkinter + SQLite 연동 구조 확립**
  - 타이머 → 세션 저장 → DB → 그래프 시각화(W3 예정)로 이어지는 데이터 흐름 완성
- **안전한 SQL 실행 패턴 학습**
  - `params` 리스트 활용한 안전한 실행 (`?` placeholder)
- **pytest의 실질적 효용성 체감**
  - 단순 성공 테스트가 아니라 “DB 동작이 의도대로 작동하는지” 보장하는 수단으로 인식
- **객체지향과 모듈화**
  - UI 로직과 DB 로직을 분리해 유지보수성과 확장성을 높임

### 다음 목표 (W3)
- DB에 저장된 세션 데이터를 기반으로 **matplotlib 주간 그래프 시각화 기능 구현**
- `fetch_daily_totals()` 결과를 이용해 요일별 공부시간 막대그래프 표시
- 누적 공부시간 및 일별 합계 표시 UI 추가 예정