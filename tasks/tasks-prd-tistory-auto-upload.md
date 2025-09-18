## Relevant Files

- `main.py` - 앱 진입점, 실행 플로우 오케스트레이션
- `gui/` (`__init__.py`, `views.py`, `dialogs.py`) - PyQt 기반 GUI 구조 및 이벤트 처리
- `automation/tistory_uploader.py` - 로그인, 글 작성, 업로드 핵심 Selenium 동작
- `automation/image_uploader.py` - 이미지 업로드 및 URL 반환 책임 분리
- `core/markdown_utils.py` - 마크다운 파싱/전처리(줄바꿈 규칙, 이미지 태그 치환)
- `core/content_builder.py` - 최종 본문 생성 파이프라인 (전처리 + 이미지 URL 매핑)
- `core/config.py` - 설정 로딩(.env, 기본값), 안전한 계정정보 접근
- `core/constants.py` - 셀렉터, URL, 타임아웃 상수 집합
- `infra/logger.py` - 구조화 로깅 설정(파일 + 콘솔)
- `infra/browser.py` - WebDriver 초기화/옵션/안정화 유틸
- `infra/exceptions.py` - 도메인 커스텀 예외 정의(LoginError 등)
- `tests/` - 유닛/통합 테스트 디렉토리
- `scripts/setup_driver.sh` - 드라이버 설치 보조 스크립트(선택)
- `README.md` - 사용/설치/문제 해결 문서
- `requirements.txt` - 의존성 관리 (Selenium, PyQt5 등)

Created scaffolding (this run):

- `main.py` - 간단한 실행 엔트리 템플릿
- `requirements.txt` - 초기 의존성 목록 (selenium, PyQt5, python-dotenv, rich, pytest)
- `gui/__init__.py` - GUI 패키지 초기화
- `gui/views.py` - PyQt 뷰 스켈레톤
- `gui/dialogs.py` - PyQt 대화상자 스켈레톤(2차 인증 안내 등)
- `core/__init__.py` - core 패키지 초기화
- `core/markdown_utils.py` - 마크다운 전처리 유틸(줄 간 가시성 보장, 이미지 경로 추출)
- `core/content_builder.py` - 컨텐츠 빌더(전처리 파이프라인)
- `automation/__init__.py` - automation 패키지 초기화
- `infra/__init__.py` - infra 패키지 초기화
- `infra/logger.py` - 기본 로거 유틸
- `.env.example` - 환경변수 예시

### Notes

- Selenium 타임아웃/재시도 정책 명시 필요 (예: explicit wait wrapper)
- 카카오 2차 인증은 자동화 불가 시 사용자 안내 다이얼로그 + 대기 루프
- 임시글 이어쓰기 팝업: 셀렉터 감지 후 닫기 → 실패 시 무시 로깅
- 이미지 업로드 속도: 순차 → 후속 최적화(병렬) 여지 표시
- 테스트 우선순위: 파싱/전처리 유틸 → 컨텐츠 빌더 → 업로더 통합(Mock)

## Tasks

MVP Focus (정상 글/이미지 업로드까지): 1.0 ~ 8.0 + 11.0 (결과 확인)
Post-MVP: 카테고리/해시태그 고급 처리, 확장 기능, 추가 테스트 범위 등

- [x] 1.0 프로젝트 초기 구조 및 환경 세팅
	- [x] 1.1 디렉토리 스캐폴딩 생성 (`gui/`, `core/`, `automation/`, `infra/`, `tests/`)
	- [x] 1.2 `requirements.txt` 초안 작성 (selenium, PyQt5, python-dotenv, rich(optional))
	- [x] 1.2 `requirements.txt` 초안 작성 (selenium, PyQt5, python-dotenv, rich(optional))
	- [x] 1.3 `.env.example` 작성 (TISTORY_ID, TISTORY_PW 등)
	- [x] 1.4 기본 `main.py` 실행 엔트리 템플릿 추가
	- [x] 1.5 개발용 README 섹션에 초기 설치 방법 작성


- [x] 2.0 로깅/에러/설정 인프라 구축
	- [x] 2.1 `infra/logger.py` 에 로거 초기화 (콘솔+파일 핸들러)
	- [x] 2.2 `infra/exceptions.py` 커스텀 예외 정의(LoginError, UploadError 등)
	- [x] 2.3 `core/config.py` 환경변수 로드 (.env → os.environ fallback)
	- [x] 2.4 설정/상수 분리 (`core/constants.py` 셀렉터/URL placeholder)
	- [x] 2.5 타임아웃/재시도 정책 상수 정의


- [x] 3.0 마크다운 전처리 및 컨텐츠 빌더 모듈
	- [x] 3.1 `markdown_utils.py` 문장 구분 및 줄바꿈 규칙 구현.
        - 구현 상세: 마크다운에서 줄 간 가시성을 보장하기 위해 빈 줄이 존재한다면 빈 줄의 존재를 보장하기 위해서 앞 줄에 `<br>` 태그를 삽입.
	    - 규칙 설명: 빈 줄이 있을 경우 앞 줄에 `<br>` 태그를 삽입하여 마크다운에서 빈 줄의 존재를 명시적으로 보장합니다.
	    - 입력 예시:
		    ```markdown
		    1줄

		    2줄
		    ```

		    위 입력은 규칙 적용 시 다음과 같이 변환됩니다:

		    ```markdown
            1줄<br>
            2줄
		    ```
	- [x] 3.2 이미지 태그/경로 파싱 함수 작성
	- [x] 3.3 `content_builder.py` (전처리 + 이미지 매핑 후 최종 문자열 생성)
	- [x] 3.4 유닛 테스트 초안 (전처리 규칙 검증)


- [x] 4.0 Selenium 브라우저/드라이버 레이어 구현
	- [x] 4.1 `infra/browser.py` WebDriver 팩토리 (ChromeOptions 설정)
	- [x] 4.2 명시적 대기 유틸 (wait_for_visible 등)
	- [x] 4.3 공용 DOM 상호작용 헬퍼 (click_js, safe_send_keys)
	- [x] 4.4 드라이버 종료/예외 처리 정리

- [x] 5.0 로그인 & 2차 인증 흐름 처리
	- [x] 5.1 로그인 페이지 이동 및 폼 요소 셀렉터 정의
	- [x] 5.2 ID/PW 입력 및 제출
	- [x] 5.3 2차 인증 발생 감지 → 사용자 안내 (GUI 다이얼로그 or 콘솔)
	- [x] 5.4 로그인 성공/실패 판별 → 실패 시 LoginError 발생

- [ ] 6.0 임시글 이어쓰기 팝업 감지/무시 처리 (실제 작성 흐름 차단 방지)
	- [ ] 6.1 팝업 존재 여부 탐지 셀렉터 정의
	- [ ] 6.2 닫기/무시 버튼 클릭 처리
	- [ ] 6.3 실패 시 경고 로그 후 정상 흐름 계속

- [ ] 7.0 이미지 업로드 및 본문 내 경로 치환 파이프라인
	- [ ] 7.1 로컬 이미지 파일 목록 스캔 (확장자 필터)
	- [ ] 7.2 티스토리 이미지 업로드 UI 진입/요소 셀렉터 정의
	- [ ] 7.3 단일 이미지 업로드 함수 구현
	- [ ] 7.4 업로드 후 URL 추출/검증
	- [ ] 7.5 마크다운 내 경로 → 업로드 URL 매핑 적용
	- [ ] 7.6 에러/재시도 정책

- [ ] 8.0 티스토리 에디터 본문 입력 & 업로드 자동화
	- [ ] 8.1 새 글 작성 페이지 진입
	- [ ] 8.2 마크다운 모드 전환
	- [ ] 8.3 제목 입력 처리
	- [ ] 8.4 본문 (전처리 결과) 붙여넣기
	- [ ] 8.5 임시 저장 또는 발행(비공개) 액션 실행
	- [ ] 8.6 업로드 완료 확인 요소/메시지 감지

- [ ] 9.0 카테고리/해시태그/공개옵션 처리 로직 (Post-MVP)
	- [ ] 9.1 카테고리 드롭다운 셀렉터 및 선택 로직
	- [ ] 9.2 해시태그 입력창 포커스 및 다중 태그 처리
	- [ ] 9.3 비공개/공개 전환 옵션 적용
	- [ ] 9.4 값 미설정 시 기본 전략 정의

- [ ] 10.0 PyQt GUI 구현 (파일 선택, 옵션 설정, 진행상태 표시)
	- [ ] 10.1 메인 윈도우 레이아웃 (파일/폴더 선택, 옵션 Form)
	- [ ] 10.2 진행 로그/상태 표시 위젯
	- [ ] 10.3 업로드 실행 스레드/비동기 처리 (GUI 프리징 방지)
	- [ ] 10.4 예외 발생 시 사용자 친화적 다이얼로그
	- [ ] 10.5 2차 인증 대기 UI 처리

- [ ] 11.0 업로드 결과/상태 리포팅 (HTTP 코드/메시지)
	- [ ] 11.1 성공/실패 표준 Result 객체 정의
	- [ ] 11.2 GUI 결과 패널 출력
	- [ ] 11.3 로그 파일 경로 안내

- [ ] 12.0 테스트 작성 (유닛 + 선택적 통합)
	- [ ] 12.1 markdown 전처리 테스트
	- [ ] 12.2 이미지 경로 매핑 테스트(Mock)
	- [ ] 12.3 content_builder 파이프라인 테스트
	- [ ] 12.4 (선택) Selenium 통합 테스트 구조 초안

- [ ] 13.0 문서화(README 확장, 사용 흐름, 문제 해결 FAQ)
	- [ ] 13.1 설치 & 실행 절차
	- [ ] 13.2 환경변수/의존성 설명
	- [ ] 13.3 일반 오류 해결(로그인 실패, 2차 인증, 셀렉터 실패)
	- [ ] 13.4 향후 개선 아이디어 섹션

- [ ] 14.0 향후 확장 포인트/백로그 정리
	- [ ] 14.1 병렬 이미지 업로드
	- [ ] 14.2 다중 파일 일괄 업로드 모드
	- [ ] 14.3 CLI 모드 추가
	- [ ] 14.4 Docker 패키징

---