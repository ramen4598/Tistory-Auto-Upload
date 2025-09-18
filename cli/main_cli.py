import os, sys
import threading
from time import sleep

from requests import get
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.constants import TISTORY_LOGIN_URL, TISTORY_HOME_URL, TISTORY_2FA_URL, TISTORY_WRITE_URL
import infra.browser as browser

def run_cli(logger):
    logger.debug('CLI 모드 진입')

    driver = init_driver(logger)
    if driver is None:return

    login_page_success = get_login_page(driver, logger)
    if not login_page_success:return

    login_success = login_tistory(driver, logger)
    if not login_success:return

    write_page_success = get_write_page(driver, logger)
    if not write_page_success:return

    sleep(60)  # TODO: 임시 대기

    # TODO 이미지 업로드
    # TODO 본문 입력
    # TODO 업로드 결과 확인
    # TODO 종료 및 정리
    logger.debug('종료')

def init_driver(logger):
    logger.info('1. 설정, 드라이버 초기화')
    try:
        driver = browser.get_chrome_driver()
    except Exception as e:
        logger.exception('드라이버 초기화 실패: %s', e)
        return None
    logger.info('드라이버 초기화 완료')
    return driver

def get_login_page(driver, logger):
    logger.info('2. 티스토리 로그인 페이지 접속')
    try:
        driver.get(TISTORY_LOGIN_URL)
        login_btn = browser.wait_for_clickable(driver, 'a.btn_login.link_kakao_id', timeout=5)
        browser.click_js(driver, login_btn)
        logger.info('티스토리 로그인 페이지 접속 완료')
    except Exception as e:
        logger.exception('티스토리 로그인 페이지 접속 실패: %s', e)
        browser.safe_quit_driver(driver)
        return False
    return True

def login_tistory(driver, logger):
    logger.info('3. 티스토리 로그인')
    try:
        # 환경 변수에서 티스토리 ID 및 비밀번호 가져오기
        TISTORY_ID = os.getenv('TISTORY_ID')
        TISTORY_PW = os.getenv('TISTORY_PW')

        # 로그인 처리 코드 (예: 아이디/비밀번호 입력 및 제출)
        id_input = browser.wait_for_clickable(driver, 'input#loginId--1', timeout=5)
        pw_input = browser.wait_for_clickable(driver, 'input#password--2', timeout=5)
        submit_btn = browser.wait_for_clickable(driver, 'div.confirm_btn>button.submit', timeout=5)
        browser.safe_send_keys(id_input, TISTORY_ID, clear_first=True)
        browser.safe_send_keys(pw_input, TISTORY_PW, clear_first=True)
        browser.click_js(driver, submit_btn)
        logger.debug('아이디/비밀번호 입력 및 제출 완료')

        # 2차 인증
        if(driver.current_url.startswith(TISTORY_2FA_URL)):
            wait_2fa_login(logger)

        # 로그인 후 대기 (특정 url로 이동했는지 확인)
        if(driver.current_url == TISTORY_HOME_URL):
            logger.info('티스토리 로그인 성공')
        else:
            raise Exception('로그인 후 메인 페이지로 이동 실패')
    except Exception as e:
        logger.exception('티스토리 로그인 실패: %s', e)
        browser.safe_quit_driver(driver)
        return False
    return True

def wait_2fa_login(logger):
    logger.info('2차 인증 요청 감지')
    print('2차 인증 필요. 최대 5분 내로 진행.')

    user_input = [None]
    stop_event = threading.Event() # 스레드 종료 신호용 이벤트

    def input_thread():
        while not stop_event.is_set():
            try:
                val = input('완료 후 y를 입력하세요: ').strip().lower()
                user_input[0] = val
                if val == 'y':
                    break
            except EOFError: # 터미널 입력이 불가한 환경 대비
                break

    # 입력을 받는 스레드 시작
    # daemon=True: 메인 스레드 종료 시 자동 종료 
    t = threading.Thread(target=input_thread, daemon=True) 
    t.start()

    cnt = 0
    while cnt < 300:
        logger.debug(user_input[0])
        if user_input[0] == 'y':
            stop_event.set()  # 스레드 종료 신호
            break
        print('경과시간 : ', cnt)
        cnt += 1
        sleep(1)
    
    if t.is_alive():
        stop_event.set()  # 스레드가 아직 실행 중이면 종료 신호
        t.join(timeout=1)  # thread 종료 대기

    if cnt >= 300: # 5분 대기
        raise Exception('2차 인증 시간 초과')

    logger.info('2차 인증 완료')
    return

def get_write_page(driver, logger):
    logger.info('4. 글 작성 페이지 이동')
    try:
        blog_name = os.getenv('TISTORY_BLOG_NAME')
        write_url = TISTORY_WRITE_URL.format(blog_name=blog_name)
        driver.get(write_url)
        logger.info('글 작성 페이지 이동 완료')
    except Exception as e:
        logger.exception('글 작성 페이지 이동 실패: %s', e)
        browser.safe_quit_driver(driver)
        return False
    return True