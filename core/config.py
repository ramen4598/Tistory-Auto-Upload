"""
core/config.py

환경변수 로드 및 접근 헬퍼
- .env 파일 자동 로드 (python-dotenv)
- os.environ fallback
- 필수값 누락 시 예외 발생
"""

import os
from dotenv import load_dotenv
from infra.exceptions import ConfigError

# .env 파일 자동 로드 (프로젝트 루트 기준)
load_dotenv()

def get_env(key: str, default=None, required: bool = False) -> str:
    """
    환경변수 조회 (.env → 시스템 환경변수)
    - required=True: 값이 없으면 ConfigError 발생
    - default: 기본값
    """
    value = os.getenv(key, default)
    if required and (value is None or value == ""):
        raise ConfigError(f"필수 환경변수 누락: {key}")
    return value

# 예시: get_env("TISTORY_ID", required=True)
