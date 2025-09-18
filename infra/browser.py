from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def wait_for_visible(driver, selector, by=By.CSS_SELECTOR, timeout=10):
    """
    지정한 셀렉터가 DOM에 나타날 때까지 명시적으로 대기합니다.
    Args:
        driver: Selenium WebDriver 인스턴스
        selector: 셀렉터 문자열
        by: 셀렉터 종류(By.CSS_SELECTOR 등)
        timeout: 최대 대기 시간(초)
    Returns:
        WebElement: 발견된 요소
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )

def wait_for_clickable(driver, selector, by=By.CSS_SELECTOR, timeout=10):
    """
    지정한 셀렉터가 클릭 가능해질 때까지 명시적으로 대기합니다.
    Args:
        driver: Selenium WebDriver 인스턴스
        selector: 셀렉터 문자열
        by: 셀렉터 종류(By.CSS_SELECTOR 등)
        timeout: 최대 대기 시간(초)
    Returns:
        WebElement: 발견된 요소
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )


def get_chrome_driver(headless: bool = True, user_agent: str = None, extra_options: dict = None):
    """
    Chrome WebDriver를 생성하고 옵션을 적용합니다.
    Args:
        headless (bool): 브라우저를 headless 모드로 실행할지 여부
        user_agent (str): 커스텀 User-Agent 문자열
        extra_options (dict): 추가 Chrome 옵션 (key-value)
    Returns:
        selenium.webdriver.Chrome: Chrome WebDriver 인스턴스
    """
    options = Options()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1280,1024') # 기본 창 크기 설정
    options.add_argument('--disable-dev-shm-usage') # /dev/shm 사용 안함
    if user_agent:
        options.add_argument(f'--user-agent={user_agent}')
    if extra_options:
        for k, v in extra_options.items():
            options.add_argument(f'--{k}={v}') 
    driver = webdriver.Chrome(options=options)
    return driver

def click_js(driver, element):
    """
    해당 요소를 JS로 클릭합니다. (일반 클릭이 실패할 때 사용)
    Args:
        driver: Selenium WebDriver 인스턴스
        element: 클릭할 WebElement
    """
    # JavaScript 코드를 실행하는 메서드
    # driver.execute_script(script, *args)
    # script 내에서 args로 전달된 요소를 참조 가능
    driver.execute_script("arguments[0].click();", element)

def safe_send_keys(element, text, clear_first=True):
    """
    요소에 텍스트를 안전하게 입력합니다. (필요시 clear)
    Args:
        element: 입력할 WebElement
        text: 입력할 문자열
        clear_first: 입력 전 clear 여부
    """
    if clear_first:
        element.clear()
    element.send_keys(text)