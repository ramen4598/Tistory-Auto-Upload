import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.markdown_utils import apply_readability_breaks

def test_apply_readability_breaks_basic():
    md = (
        "1줄\n"
        "\n"
        "2줄"
    )
    result = apply_readability_breaks(md, enabled=True)
    # 빈 줄 뒤에 두 공백+개행이 들어갔는지 확인
    assert result == (
        "1줄  \n"
        "\n"
        "\n"
        "2줄"
    )

def test_apply_readability_breaks_disabled():
    md = (
        "1줄\n"
        "\n"
        "2줄"
    )
    result = apply_readability_breaks(md, enabled=False)
    assert result == md

def test_apply_readability_breaks_multiple_blanks():
    md = (
        "1줄\n"
        "\n"
        "\n"
        "2줄"
    )
    result = apply_readability_breaks(md, enabled=True)
    # 연속 빈 줄도 모두 변환되는지 확인
    assert result == (
        "1줄  \n"
        "\n"
        "  \n"
        "\n"
        "\n"
        "2줄"
    )
