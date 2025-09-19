import re


def apply_readability_breaks(md_text: str, enabled: bool = False) -> str:
    """ 
    마크다운에서 줄 간 가시성을 보장하기 위해 빈 줄이 존재한다면 빈 줄의 존재를 보장하기 위해서 앞 줄에 `<br>` 태그를 삽입.
	- 규칙 설명: 빈 줄이 있을 경우 앞 줄에 `<br>` 태그를 삽입하여 마크다운에서 빈 줄의 존재를 명시적으로 보장합니다.
	- 입력 예시:
		```markdown
		1줄

		2줄
		```

		위 입력은 규칙 적용 시 다음과 같이 변환됩니다:

		```markdown
        1줄<br>
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

        result[-1] = result[-1] + "<br>"  # 이전 줄 끝에 <br> 추가

    return "\n".join(result)

def extract_local_image_paths(md_text: str) -> list:
    """마크다운에서 로컬 이미지 경로를 추출합니다. 간단한 regex 사용."""
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    return re.findall(pattern, md_text)

