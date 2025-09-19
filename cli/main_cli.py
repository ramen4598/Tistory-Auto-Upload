import os
import sys
import threading
from selenium.common.exceptions import TimeoutException
from time import sleep

from infra.exceptions import LoginError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.constants import TISTORY_LOGIN_URL, TISTORY_HOME_URL, TISTORY_2FA_URL, TISTORY_WRITE_URL
import infra.browser as browser

def run_cli(logger, file_path):
    logger.debug('CLI 모드 진입')

    try:
        driver = init_driver(logger)
    except Exception as e:
        logger.exception(e)
        return
    
    try:
        get_login_page(driver, logger)     
        login_tistory(driver, logger)
        get_write_page(driver, logger)
        ignore_alert(driver, logger)
        markdown_content = read_markdown_file(logger, file_path)
        image_url_map = upload_image(driver, logger, markdown_content)
        input_content(driver, logger, markdown_content, image_url_map)
        add_new_post(driver, logger)
        sleep(60) # TODO: 디버깅용 임시 대기. 나중에 제거.
    except Exception as e:
        logger.exception(e)
    finally:
        browser.safe_quit_driver(driver)

    logger.debug('종료')


def init_driver(logger):
    logger.info('1. 설정, 드라이버 초기화')
    try:
        driver = browser.get_chrome_driver()
        if driver is None:
            raise Exception('크롬 드라이버 초기화 실패')
    except Exception as e:
        raise Exception('드라이버 초기화 실패') from e
    return driver

def get_login_page(driver, logger):
    logger.info('2. 티스토리 로그인 페이지 접속')
    try:
        driver.get(TISTORY_LOGIN_URL)
        login_btn = browser.wait_for_clickable(driver, 'a.btn_login.link_kakao_id', timeout=5)
        browser.click_js(driver, login_btn)
    except Exception as e:
        raise Exception('티스토리 로그인 페이지 접속 실패') from e

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
        if driver.current_url.startswith(TISTORY_2FA_URL):
            wait_2fa_login(logger)

        # 로그인 후 대기 (특정 url로 이동했는지 확인)
        if driver.current_url.startswith(TISTORY_HOME_URL):
            logger.info('티스토리 로그인 성공')
        else:
            raise LoginError('로그인 후 메인 페이지로 이동 실패')
    except Exception as e:
        raise LoginError('티스토리 로그인 실패') from e

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
        if user_input[0] == 'y':
            stop_event.set()  # 스레드 종료 신호
            break
        print('경과시간 : ', cnt) # 사용자 입력 대기 중임을 알리기 위한 출력
        cnt += 1
        sleep(1)
    
    if t.is_alive():
        stop_event.set()  # 스레드가 아직 실행 중이면 종료 신호
        t.join(timeout=1)  # thread 종료 대기

    if cnt >= 300: # 5분 대기
        raise LoginError('2차 인증 시간 초과')

    logger.info('2차 인증 완료')
    return

def get_write_page(driver, logger):
    logger.info('4. 글 작성 페이지 이동')
    try:
        blog_name = os.getenv('TISTORY_BLOG_NAME')
        write_url = TISTORY_WRITE_URL.format(blog_name=blog_name)
        driver.get(write_url)
    except Exception as e:
        raise Exception('글 작성 페이지 이동 실패') from e

def ignore_alert(driver, logger):
    try:
        alert = browser.wait_for_alert(driver, timeout=3)
    except TimeoutException:
        return

    logger.info('5. 임시글 이어쓰기 팝업 무시')
    try:
        alert.dismiss()  # 팝업 무시 (취소)
        logger.debug('임시글 이어쓰기 팝업 무시 완료')
    except Exception as e:
        raise Exception('임시글 이어쓰기 팝업 무시 실패') from e

def read_markdown_file(logger, file_path):
    logger.info('마크다운 파일 읽기')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logger.debug('마크다운 파일 읽기 완료')
        return content
    except Exception as e:
        raise Exception('마크다운 파일 읽기 실패') from e

def upload_image(driver, logger, markdown_content):
    logger.info('6. 이미지 업로드')
    logger.debug(markdown_content)
    result = {}
    # TODO 이미지 업로드
    # 마크다운 파일 읽기
    # 로컬 이미지 경로 추출
    # 이미지 업로드
    # 업로드된 이미지 URL 추출
    # image_url_map (dict): {로컬경로: 업로드URL} 매핑 수행
    return result

def input_content(driver, logger, markdown_content, image_url_map):
    logger.info('7. 본문 입력')
    logger.debug(image_url_map)
    # TODO 본문 입력
    # markdown editor iframe 전환
    # ContentBuilder 인스턴스 생성
    # ContentBuilder.build() 사용
    # editor에 본문 입력
    # iframe 벗어나기

def add_new_post(driver, logger):
    logger.info('새 글 작성 버튼 클릭')
    # TODO: 새글 작성 완료
    # 비공개 업로드
    # 업로드 결과 확인