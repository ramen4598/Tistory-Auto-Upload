import re


def apply_readability_breaks(md_text: str, enabled: bool = False) -> str:
    """ 
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
    """
    if not enabled:
        return md_text

    lines = md_text.splitlines()
    result = []
    for i, line in enumerate(lines):
        # 첫 줄이거나 빈 줄이 아닐 경우 그냥 추가
        if  i == 0 or line.strip() != "":
            result.append(line)
            continue

        result[-1] = result[-1] + "  "  # 이전 줄 끝에 두 공백 추가
        result.append("") # 현재 빈 줄 추가
        result.append("") # 두번째 빈 줄 추가

    return "\n".join(result)

def parse_image_paths(markdown_text):
    """
    마크다운 텍스트에서 이미지 경로(로컬 파일 포함)를 추출합니다.
    예: ![alt](./img/foo.png) → './img/foo.png' 반환
    Args:
        markdown_text (str): 마크다운 원본 텍스트
    Returns:
        List[str]: 추출된 이미지 경로 리스트
    """
    # ![...](경로) 패턴 매칭
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    return re.findall(pattern, markdown_text)

def extract_local_image_paths(md_text: str) -> list:
    """마크다운에서 로컬 이미지 경로를 추출합니다. 간단한 regex 사용."""
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    return re.findall(pattern, md_text)

