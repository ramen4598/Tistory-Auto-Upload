import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.content_builder import ContentBuilder

def test_build_with_image_url_map_and_readability():
    md = (
        "1줄\n"
        "\n"
        "2줄\n"
        "![img1](./foo.png)\n"
        "텍스트\n"
        "![img2](../bar.jpg)"
    )
    image_url_map = {
        "./foo.png": "https://cdn.com/foo.png",
        "../bar.jpg": "https://cdn.com/bar.jpg"
    }
    builder = ContentBuilder(md)
    result = builder.build(image_url_map=image_url_map, readability_breaks=True)
    assert result == (
        "1줄<br>\n"
        "2줄\n"
        "![img1](https://cdn.com/foo.png)\n"
        "텍스트\n"
        "![img2](https://cdn.com/bar.jpg)"
    )


def test_build_without_image_url_map():
    md = "텍스트\n![img](img.png)"
    builder = ContentBuilder(md)
    result = builder.build(image_url_map=None, readability_breaks=False)
    assert result == md

def test_build_with_partial_image_url_map():
    md = "![img1](foo.png)\n![img2](bar.png)"
    image_url_map = {"foo.png": "http://a.com/foo.png"}
    builder = ContentBuilder(md)
    result = builder.build(image_url_map=image_url_map, readability_breaks=False)
    assert result == "![img1](http://a.com/foo.png)\n![img2](bar.png)"
