# Tistory Automation

- 티스토리 블로그에 자동으로 글 업로드.

---
## 요구사항

- [ ] 자동 로그인
- [ ] 마크다운 파일을 읽어서 마크다운 에디터에 입력
- [ ] 이미지 업로드
- [ ] 마크다운에서 줄 간 가시성을 보장하기 위해 빈 줄이 존재한다면 빈 줄의 존재를 보장하기 위해서 앞 줄에 `<br>` 태그를 삽입.
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
- [ ] 관리자 검토를 위해서 비공개 업로드
- [ ] 카테고리 선택
- [ ] 해쉬태그 관련 키워드 입력

---
## 기술 스택

- Python
- Selenium

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 설치 및 실행 (개발용)

다음은 로컬 개발 환경에서 프로젝트를 설정하고 실행하는 기본 가이드입니다.

1. 파이썬 가상환경 생성 (권장)

```bash
# macOS / zsh 예시
# 개발 당시 python 3.13.7 사용
python3 -m venv .venv
source .venv/bin/activate
```

2. 의존성 설치
```bash
brew install qt
pip install --upgrade pip
pip install -r requirements.txt
```

3. `.env` 파일 설정

```bash
cp .env.example .env
# 편집하여 TISTORY_ID, TISTORY_PW, TISTORY_BLOG_NAME 등을 채워주세요
```

4. 브라우저 드라이버

프로젝트는 Selenium과 `webdriver-manager`를 사용하여 드라이버를 자동으로 관리합니다. 추가 설정이 필요하면 `infra/browser.py`에 맞게 환경을 조정하세요.

5. 실행

일반적으로 GUI 없이 스크립트 모드로 실행하거나 GUI 모드로 실행할 수 있습니다.

```bash
# CLI 모드 (GUI 미사용)
python main.py --no-gui

# GUI 모드 (PyQt 기반, 향후 구현)
python main.py --gui
```

6. 테스트 실행

```bash
pytest -q
```

7. 개발 노트

- `.env`에는 민감한 정보가 포함되므로 절대 버전 관리에 커밋하지 마세요.
- 첫 실행 시, 브라우저 자동 로그인/2차 인증 흐름은 수동 입력이 필요할 수 있습니다.
- 로깅은 `infra/logger.py`로 초기화되며, 파일 핸들러은 추후 설정됩니다.
