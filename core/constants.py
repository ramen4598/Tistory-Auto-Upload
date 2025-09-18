"""
core/constants.py

티스토리 자동화에서 사용하는 주요 상수 (셀렉터, URL, 타임아웃 등)
- 실제 값은 개발/테스트 과정에서 보완
"""

# URL
from re import T


TISTORY_LOGIN_URL = "https://www.tistory.com/auth/login"
TISTORY_WRITE_URL = "https://{blog_name}.tistory.com/manage/newpost/"
TISTORY_HOME_URL = "https://www.tistory.com/"
TISTORY_2FA_URL = "https://accounts.kakao.com/login/"

# 셀렉터 (예시, 실제 값은 개발 중 보완)
SELECTOR_ID_INPUT = "input#loginId"
SELECTOR_PW_INPUT = "input#loginPw"
SELECTOR_LOGIN_BTN = "button[type='submit']"
SELECTOR_EDITOR_BODY = "div.editor-body textarea, div.editor-body [contenteditable='true']"
SELECTOR_IMAGE_UPLOAD_BTN = "button[aria-label='이미지']"
SELECTOR_IMAGE_INPUT = "input[type='file']"


# 타임아웃/재시도 정책 (초/회)
DEFAULT_TIMEOUT = 2  # 기본 명시적 대기(Explicit Wait) 타임아웃
IMAGE_UPLOAD_TIMEOUT = 20  # 이미지 업로드 최대 대기
LOGIN_TIMEOUT = 10  # 로그인 시도 최대 대기
POPUP_HANDLE_TIMEOUT = 5  # 팝업 감지/처리 대기

# 재시도 정책
RETRY_COUNT = 3  # 기본 재시도 횟수
RETRY_INTERVAL = 2  # 재시도 간격(초)
IMAGE_UPLOAD_RETRY = 2  # 이미지 업로드 재시도 횟수

# 기타

# 기타
MAX_IMAGE_SIZE_MB = 10

# TODO: 실제 셀렉터/URL/상수 및 정책은 개발 과정에서 보완 및 확정
