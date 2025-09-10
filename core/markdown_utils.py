import re


def apply_readability_breaks(md_text: str, enabled: bool = False) -> str:
    """(Stub) 
    마크다운에서 줄 간 가시성을 보장하기 위해 두 줄 사이 빈 줄이 존재한다면 빈 줄의 존재를 보장하기 위해서 두 줄 사이에 두개의 공백과 두번의 개행을 삽입.
	- 규칙 설명: "줄과 줄 사이에 빈 줄이 있을 경우" 두 줄 사이에 두 공백을 추가하고 두번 개행하여 마크다운에서 빈 줄의 존재를 명시적으로 보장합니다.
	- 입력 예시:
		```markdown
		1줄

		2줄
		```

		위 입력은 규칙 적용 시 다음과 같이 변환됩니다:

		```markdown
        1줄  


        2줄
		```
    현재 구현은 비워두고 원문을 그대로 반환합니다. 실제 전처리 로직은 추후 구현됩니다.
    """
    if not enabled:
        return md_text

    # TODO: 실제 전처리 로직 구현
    return md_text


def extract_local_image_paths(md_text: str) -> list:
    """마크다운에서 로컬 이미지 경로를 추출합니다. 간단한 regex 사용."""
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    return re.findall(pattern, md_text)
