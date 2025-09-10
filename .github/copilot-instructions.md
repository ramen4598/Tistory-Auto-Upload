# Copilot Instructions for Tistory-Auto-Upload

## Project Overview

**Tistory-Auto-Upload** is a Python automation tool for uploading blog posts to Tistory (Korean blogging platform). The project uses Selenium WebDriver to automate browser interactions for logging in, uploading markdown content, managing images, and configuring post settings.

**Repository Information:**
- **Language**: Python
- **Framework**: Selenium WebDriver
- **Target Platform**: Tistory (tistory.com)
- **Content Format**: Markdown
- **Repository Size**: Small (early development stage)
- **License**: MIT

## Project Requirements & Features

Based on the README.md, the system must implement:
- Automatic login to Tistory
- Read markdown files and input to markdown editor
- Image upload functionality
- Text formatting (line breaks after sentences, excluding markdown elements)
- Private post upload for admin review
- Category selection
- Hashtag/keyword input

## Development Environment Setup

### Prerequisites
Always install these dependencies before development:

```bash
# Create virtual environment (always recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install selenium
pip install beautifulsoup4  # For HTML parsing
pip install requests       # For HTTP requests
pip install markdown      # For markdown processing
```

### WebDriver Setup
**Critical**: Selenium requires browser drivers. Install ChromeDriver or GeckoDriver:
```bash
# For Chrome (recommended)
pip install webdriver-manager
# This package auto-manages driver downloads
```

### Project Structure
The expected project layout should be:
```
├── src/
│   ├── __init__.py
│   ├── tistory_uploader.py    # Main automation logic
│   ├── markdown_processor.py  # Markdown file processing
│   ├── image_handler.py       # Image upload functionality
│   └── config.py              # Configuration management
├── tests/
│   ├── __init__.py
│   ├── test_uploader.py
│   └── test_markdown_processor.py
├── config/
│   └── settings.py            # Settings and credentials
├── requirements.txt
├── setup.py
└── README.md
```

## Build and Development Commands

### Environment Setup (Run First)
```bash
# Always run these commands in order:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # After creating requirements.txt
```

### Testing Commands
Since this is a web automation project, testing requires special considerations:
```bash
# Unit tests (fast, no browser)
python -m pytest tests/unit/ -v

# Integration tests (requires browser, slower)
python -m pytest tests/integration/ -v --headless

# Full test suite (can take 2-3 minutes)
python -m pytest tests/ -v
```

### Linting and Code Quality
```bash
# Code formatting
black src/ tests/
flake8 src/ tests/

# Type checking (if using type hints)
mypy src/
```

### Running the Application
```bash
# Basic usage
python -m src.tistory_uploader --file path/to/markdown.md

# With configuration
python -m src.tistory_uploader --config config/settings.py --file path/to/markdown.md
```

## Critical Development Considerations

### Security and Credentials
**NEVER commit credentials to git**. Always use:
- Environment variables for sensitive data
- `.env` files (add to .gitignore)
- Separate config files outside repository

Example secure credential handling:
```python
import os
from dotenv import load_dotenv

load_dotenv()
TISTORY_USERNAME = os.getenv('TISTORY_USERNAME')
TISTORY_PASSWORD = os.getenv('TISTORY_PASSWORD')
```

### Selenium Best Practices
- Always use explicit waits, not sleep()
- Implement retry logic for flaky web elements
- Use headless mode for CI/CD
- Handle popup windows and alerts
- Close browser sessions properly in finally blocks

### Korean Language Support
- Use UTF-8 encoding for all file operations
- Test with Korean markdown content
- Handle Korean IME (Input Method Editor) if needed
- Verify Korean text rendering in browser

### Common Failure Points and Solutions

**Browser Driver Issues**:
```bash
# If driver not found, install webdriver-manager
pip install webdriver-manager
# Use in code: from webdriver_manager.chrome import ChromeDriverManager
```

**Selenium TimeoutException**:
- Increase wait times for slow network connections
- Use WebDriverWait with expected_conditions
- Check for pop-ups or modal dialogs blocking interaction

**Korean Text Encoding Issues**:
```python
# Always specify encoding when reading files
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
```

## Testing Strategy

### Unit Tests
Test individual components without browser:
- Markdown processing functions
- Configuration parsing
- Text formatting utilities

### Integration Tests
Test with actual browser (use CI-friendly options):
```python
# For CI/CD, always use headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
```

### Manual Testing Checklist
Before committing changes, manually verify:
- Login process works with test credentials
- Markdown content renders correctly
- Images upload successfully
- Korean text displays properly
- Post categorization functions
- Private/public post settings work

## GitHub Actions / CI Considerations

For future CI/CD setup:
- Use Ubuntu latest runner
- Install Chrome/ChromeDriver in CI
- Use environment secrets for credentials
- Run tests in headless mode
- Set appropriate timeouts (selenium tests can be slow)

Example workflow needs:
```yaml
- name: Install Chrome
  uses: browser-actions/setup-chrome@latest
- name: Install dependencies
  run: |
    pip install -r requirements.txt
- name: Run tests
  run: pytest --headless --timeout=300
  env:
    TISTORY_USERNAME: ${{ secrets.TISTORY_USERNAME }}
    TISTORY_PASSWORD: ${{ secrets.TISTORY_PASSWORD }}
```

## File Locations and Key Components

**Configuration Files**:
- `.gitignore`: Should exclude venv/, __pycache__/, .env, *.log
- `requirements.txt`: Python dependencies
- `.env.example`: Template for environment variables

**Core Source Files**:
- Main automation logic in `src/tistory_uploader.py`
- Markdown processing in `src/markdown_processor.py`
- Browser automation utilities in `src/browser_utils.py`
- Configuration management in `src/config.py`

## Instructions for Coding Agents

**Trust these instructions** and avoid extensive exploration unless:
1. Information here is incomplete or contradictory
2. You encounter errors not documented here
3. Requirements have changed significantly

**Always**:
- Set up virtual environment before installing packages
- Use explicit waits in Selenium code
- Handle Korean text with UTF-8 encoding
- Test with actual Tistory website behavior
- Validate credentials are not committed to git
- Run tests in headless mode for CI compatibility

**Common Time Wasters to Avoid**:
- Don't spend time searching for existing build scripts (none exist yet)
- Don't look for existing test infrastructure (needs to be created)
- Don't search for CI configuration (none exists)
- Focus on implementing the core automation features listed in README.md

This is an early-stage project - expect to create foundational structure and tooling as you implement features.