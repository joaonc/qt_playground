import logging
import sys

from PySide6.QtWidgets import QApplication

from src.ui.playground_main_window import PlaygroundMainWindow
import src.update.update as update
import src.config as config
from pathlib import Path


def main():
    if not config.check_update_only:
        # Launch UI
        app = QApplication()
        window = PlaygroundMainWindow()
        window.show()
        app_response = app.exec()
        if app_response != 0:
            logging.error(f'An error occurred. Exiting with status {app_response}.')
            if not config.no_check_update:
                logging.warning('Not checking for app update.')
            sys.exit(app_response)

    if not config.no_check_update or config.check_update_only:
        try:
            # update_manifest = Path(__file__).parent / 'app.yaml'
            need_update, version_update = update.check_update(config.update_manifest)
        except FileNotFoundError:
            logging.warning(
                f'Manifest for file to update not found: {config.update_manifest}\n'
                f'Not performing an update check.'
            )
            need_update, version_update = False, None

        if need_update:
            logging.info(f'Performing update to version {version_update}.')
            try:
                update.perform_update(config.update_file)
            except FileNotFoundError:
                logging.warning(f'File {config.update_file} not found. Update failed.')


def set_config_values():
    from argparse import ArgumentParser, BooleanOptionalAction, RawTextHelpFormatter

    description = f'Qt Playground {config.version}'

    parser = ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        '--no-check-update',
        action=BooleanOptionalAction,
        default=False,
        help='Do not check for app updates.',
    )
    parser.add_argument(
        '--check-update-only',
        action=BooleanOptionalAction,
        default=False,
        help='Only check for updates and do not launch the app.',
    )
    parser.add_argument(
        '--update-manifest',
        type=str,
        help='App manifest file. Used to check for updates.',
    )
    parser.add_argument(
        '--update-file',
        type=str,
        help='Path to new file to update to.',
    )
    parser.add_argument(
        '--log-level',
        choices=[level.lower() for level in logging.getLevelNamesMapping()],
        default='info',
        help='Log level to use.',
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=str(config.version),
    )

    args = parser.parse_args()

    logging.basicConfig(level=logging.getLevelName(args.log_level.upper()))
    logging.debug(f'App version {config.version}. Log level {args.log_level}.')

    config.no_check_update = args.no_check_update
    config.check_update_only = args.check_update_only
    if args.update_manifest:
        config.update_manifest = args.update_manifest
    if args.update_file:
        config.update_file = args.update_file


if __name__ == '__main__':
    set_config_values()
    main()
