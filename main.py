import sys
import argparse
from infra.logger import get_logger


# Entrypoint for Tistory Auto Upload
def build_arg_parser():
    p = argparse.ArgumentParser(description='Tistory Auto Upload - 간단 실행기')
    p.add_argument('--gui', dest='use_gui', action='store_true', help='Run with PyQt GUI')
    p.add_argument('--no-gui', dest='use_gui', action='store_false', help='Run in headless/script mode')
    p.set_defaults(use_gui=True)
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
        # TODO: GUI 초기화 로직 호출 (gui.views.MainView 등)
    else:
        logger.info('비-GUI(스크립트) 모드로 실행합니다')
        # TODO: 스크립트 모드 실행 로직


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger = get_logger()
        logger.exception('예외로 종료: %s', e)
        sys.exit(1)
