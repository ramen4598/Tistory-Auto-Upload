from re import T
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.constants import TISTORY_LOGIN_URL
import infra.browser as browser

def run_cli(logger):
    logger.info('CLI 모드 진입')
    # TODO: 스크립트 모드 실행 로직
    driver = browser.get_chrome_driver(headless=False)
    driver.get(TISTORY_LOGIN_URL)

    # TODO 로그인
    # TODO 이미지 업로드
    # TODO 본문 입력
    # TODO 업로드 결과 확인
    # TODO 종료 및 정리
    logger.info('종료')