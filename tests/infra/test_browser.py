import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from infra import browser

class DummyDriver:
    def __init__(self):
        self.quit_called = False
        self.script = None
    def quit(self):
        self.quit_called = True
    def execute_script(self, script, element):
        self.script = (script, element)

class DummyElement:
    def __init__(self):
        self.cleared = False
        self.sent_text = None
    def clear(self):
        self.cleared = True
    def send_keys(self, text):
        self.sent_text = text

def test_safe_quit_driver():
    driver = DummyDriver()
    browser.safe_quit_driver(driver)
    assert driver.quit_called is True

def test_click_js():
    driver = DummyDriver()
    elem = object()
    browser.click_js(driver, elem)
    assert driver.script == ("arguments[0].click();", elem)

def test_safe_send_keys_clear():
    elem = DummyElement()
    browser.safe_send_keys(elem, "hello", clear_first=True)
    assert elem.cleared is True
    assert elem.sent_text == "hello"

def test_safe_send_keys_no_clear():
    elem = DummyElement()
    browser.safe_send_keys(elem, "world", clear_first=False)
    assert elem.cleared is False
    assert elem.sent_text == "world"
