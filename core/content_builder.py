from .markdown_utils import normalize_paragraphs, extract_local_image_paths

class ContentBuilder:
    def __init__(self, md_text: str):
        self.md_text = md_text
        self.image_paths = extract_local_image_paths(md_text)

    def build(self):
        # 현재는 전처리만 적용
        return normalize_paragraphs(self.md_text)
