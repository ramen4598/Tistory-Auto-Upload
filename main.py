from ast import arg
import sys
import argparse
import core.config as config
from infra.logger import get_logger


# Entrypoint for Tistory Auto Upload
def build_arg_parser():
    p = argparse.ArgumentParser(description='Tistory Auto Upload - 간단 실행기')
    p.add_argument('--gui', dest='use_gui', action='store_true', help='Run with PyQt GUI')
    p.add_argument('--no-gui', dest='use_gui', action='store_false', help='Run in headless/script mode')
    p.add_argument('--file-path', type=str, help='Path to the markdown file to upload (required in non-GUI mode)')
    p.set_defaults(use_gui=False)
    p.set_defaults(file_path=None)
    return p


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    logger = get_logger()
    logger.info('Tistory Auto Upload 시작')
    logger.debug('Args: %s', args)

    if args.use_gui:
        logger.info('GUI 모드로 실행합니다 (PyQt)')
        import gui.main_gui as main_gui
        main_gui.run_gui(logger)
    else:
        if args.file_path is None:
            logger.error('마크다운 파일 경로가 지정되지 않았습니다. --file-path 인자를 사용하세요.')
            sys.exit(1)

        logger.info('비-GUI(스크립트) 모드로 실행합니다')
        import cli.main_cli as main_cli
        main_cli.run_cli(logger, args.file_path)

    logger.info('종료')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger = get_logger()
        logger.exception('예외로 종료: %s', e)
        sys.exit(1)
