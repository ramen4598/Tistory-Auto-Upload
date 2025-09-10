import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name: str = "tistory_auto_upload") -> logging.Logger:
	"""
	프로젝트 전역 로거 생성 (콘솔+파일 핸들러, 회전)
	- 로그 레벨: LOG_LEVEL(.env) 또는 INFO
	- 로그 파일: LOG_FILE(.env) 또는 logs/tistory.log
	- 파일 회전: 2MB, 3개 백업
    콘솔+파일 둘 다 함께 사용하면 개발(실시간 확인)과 운영(기록/분석) 모두에 유리함
	"""

	logger = logging.getLogger(name)
	if getattr(logger, "_is_configured", False):
		return logger

	log_level = os.getenv("LOG_LEVEL", "INFO").upper()
	log_file = os.getenv("LOG_FILE", "logs/tistory.log")
	os.makedirs(os.path.dirname(log_file), exist_ok=True)

	formatter = logging.Formatter(
		fmt="%(asctime)s [%(levelname)s] %(name)s | %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S"
	)

    # 콘솔 핸들러: 로그를 터미널(실행창)에 출력하여 실시간 확인 및 디버깅에 유용함
	ch = logging.StreamHandler()
	ch.setFormatter(formatter)
	logger.addHandler(ch)

    # 파일 핸들러: 로그를 파일로 저장하여 실행 이력, 에러, 경고 등을 장기적으로 기록 및 분석 가능
	fh = RotatingFileHandler(log_file, maxBytes=2*1024*1024, backupCount=3, encoding="utf-8")
	fh.setFormatter(formatter)
	logger.addHandler(fh)

	logger.setLevel(getattr(logging, log_level, logging.INFO))
	logger._is_configured = True
	return logger