"""
core/constants.py

티스토리 자동화에서 사용하는 주요 상수 (셀렉터, URL, 타임아웃 등)
- 실제 값은 개발/테스트 과정에서 보완
"""

# URL
TISTORY_LOGIN_URL = "https://www.tistory.com/auth/login"
TISTORY_WRITE_URL = "https://{blog_name}.tistory.com/manage/post/write"

# 셀렉터 (예시, 실제 값은 개발 중 보완)
SELECTOR_ID_INPUT = "input#loginId"
SELECTOR_PW_INPUT = "input#loginPw"
SELECTOR_LOGIN_BTN = "button[type='submit']"
SELECTOR_EDITOR_BODY = "div.editor-body textarea, div.editor-body [contenteditable='true']"
SELECTOR_IMAGE_UPLOAD_BTN = "button[aria-label='이미지']"
SELECTOR_IMAGE_INPUT = "input[type='file']"

# 타임아웃/대기 (초)
DEFAULT_TIMEOUT = 10
IMAGE_UPLOAD_TIMEOUT = 30

# 기타
MAX_IMAGE_SIZE_MB = 10

# TODO: 실제 셀렉터/URL/상수는 개발 과정에서 보완 및 확정
