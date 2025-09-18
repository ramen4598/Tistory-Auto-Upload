
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from core.markdown_utils import parse_image_paths

def test_parse_image_paths_basic():
    md = """
    ![img1](./foo.png)
    텍스트
    ![img2](../bar.jpg)
    ![img3](https://example.com/img.png)
    """
    result = parse_image_paths(md)
    assert result == ["./foo.png", "../bar.jpg", "https://example.com/img.png"]

def test_parse_image_paths_no_images():
    md = "텍스트만 있습니다."
    result = parse_image_paths(md)
    assert result == []

def test_parse_image_paths_mixed_content():
    md = """
    ![alt1](img1.jpg)
    ![alt2](img2.png)
    [링크](https://naver.com)
    ![alt3](../img3.gif)
    """
    result = parse_image_paths(md)
    assert result == ["img1.jpg", "img2.png", "../img3.gif"]
