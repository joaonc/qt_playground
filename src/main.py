import logging
import sys
import types
from pathlib import Path

from PySide6.QtWidgets import QApplication

import src.config as config
import src.update.update as update
from src.ui.playground_main_window import PlaygroundMainWindow


def main():
    # Launch UI
    if not config.check_update_only:
        app = QApplication()
        window = PlaygroundMainWindow()
        window.show()
        app_response = app.exec()
        if app_response != 0:
            logging.error(f'An error occurred. Exiting with status {app_response}.')
            sys.exit(app_response)

    # Update
    if config.check_update or config.check_update_only:
        try:
            need_update, version_update = update.check_update(config.update_manifest)
            if version_update is None:
                logging.warning('Manifest file to update not specified.')
        except FileNotFoundError:
            logging.warning(
                f'Manifest for file to update not found: {config.update_manifest}\n'
                f'Not checking for app update.'
            )
            need_update, version_update = False, None

        if need_update:
            logging.info(f'Updating to version {version_update}.')

            try:
                update.perform_update()
                logging.info(
                    'Update was successful and the new version will be used the next time '
                    'the app runs.'
                )
            except Exception as e:
                logging.warning(f'Error updating.\n{e}')
        else:
            logging.info('No update required.')
    else:
        logging.info('Not checking for app update.')


def set_config_values():
    from argparse import ArgumentParser, BooleanOptionalAction, RawTextHelpFormatter

    description = f'Qt Playground {config.version}'

    parser = ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        '--check-update',
        action=BooleanOptionalAction,
        default=True,
        help='Check for app updates.',
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
        # Can use `logging.getLevelNamesMapping()` instead of `_nameToLevel` on python 3.11+
        choices=[level.lower() for level in logging._nameToLevel],  # noqa
        default='error',
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
    logging.debug(
        f'Qt Playground.\n  App version: {config.version}\n  Log level: {args.log_level}\n  '
        f'File: {sys.executable}'
    )

    config.check_update = args.check_update
    config.check_update_only = args.check_update_only
    if args.update_manifest:
        config.update_manifest = Path(args.update_manifest).resolve(strict=False)
    if args.update_file:
        config.update_file = Path(args.update_file).resolve(strict=False)

    # Config contents
    config_dict = {
        key: getattr(config, key, '__UNDEFINED__')
        for key in sorted(dir(config))
        if (
            not key.startswith('_')
            and (  # noqa: W503
                type(getattr(config, key))
                not in [
                    types.FunctionType,
                    types.ModuleType,
                    type,
                ]
            )
        )
    }
    logging.debug('Config:\n' + '\n'.join(f'  {key}: {val}' for key, val in config_dict.items()))


if __name__ == '__main__':
    set_config_values()
    main()
    logging.debug('App exiting.')
