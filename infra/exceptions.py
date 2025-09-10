"""
infra/exceptions.py

도메인 특화 예외 정의: 로그인, 업로드, 인증 등
"""

class TistoryAutomationError(Exception):
    """기본 도메인 예외 (모든 커스텀 예외의 부모)"""
    pass

class LoginError(TistoryAutomationError):
    """로그인 실패/2차 인증 등 로그인 관련 예외"""
    pass

class ImageUploadError(TistoryAutomationError):
    """이미지 업로드 실패 등 이미지 관련 예외"""
    pass

class PostUploadError(TistoryAutomationError):
    """글 전체 업로드 실패 등 포스트 관련 예외"""
    pass

class PopupHandleError(TistoryAutomationError):
    """임시글 이어쓰기 팝업 등 예외 상황 처리 실패"""
    pass

class ConfigError(TistoryAutomationError):
    """환경설정/필수값 누락 등 설정 관련 예외"""
    pass
