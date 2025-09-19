import re
from .markdown_utils import apply_readability_breaks, extract_local_image_paths


class ContentBuilder:
    def __init__(self, md_text: str, image_url_map: dict = None):
        self.md_text = md_text
        self.image_url_map = image_url_map  # {local: url}

    def build(self, readability_breaks=True):
        """
        전처리(줄바꿈 규칙) + 이미지 경로 → 업로드 URL 매핑 적용 후 최종 문자열 반환
        Args:
            readability_breaks (bool): 줄 간 가시성 보장 규칙 적용 여부
        Returns:
            str: 최종 변환된 마크다운
        """
        text = self.md_text
        image_url_map = self.image_url_map
        if image_url_map:
            for local_path, url in image_url_map.items():
                # ![...](local_path) → ![...](url)로 치환
                pattern = r'(!\[[^\]]*\]\()' + re.escape(local_path) + r'(\))'
                text = re.sub(pattern, r'\1' + url + r'\2', text)
        # 줄바꿈 전처리
        content = apply_readability_breaks(text, enabled=readability_breaks)
        return content