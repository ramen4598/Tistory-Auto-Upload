import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from core.markdown_utils import apply_readability_breaks

# 빈 줄 뒤에 <br>이 들어갔는지 확인
def test_apply_readability_breaks_basic():
    # 1줄
    # 
    # 2줄
    md = "1줄\n\n2줄"
    result = apply_readability_breaks(md, enabled=True)
    # 1줄<br>
    # 2줄
    assert result == "1줄<br>\n2줄"

# 비활성화 시 원본 유지
def test_apply_readability_breaks_disabled():
    # 1줄
    #
    # 2줄
    md = "1줄\n\n2줄"
    result = apply_readability_breaks(md, enabled=False)
    assert result == md

# 연속 빈 줄도 모두 변환되는지 확인
def test_apply_readability_breaks_multiple_blanks():
    # 1줄
    #
    #
    # 2줄
    md = "1줄\n\n\n2줄"
    result = apply_readability_breaks(md, enabled=True)
    # 1줄<br><br>
    # 2줄
    assert result == "1줄<br><br>\n2줄"
