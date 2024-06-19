import shutil
import sys

from semantic_version import Version

import src.config as config


def check_update(update_manifest=None) -> tuple[bool, Version | None]:
    """
    Check if there's a newer version of the app.

    :param update_manifest: The new app's  manifest file location.

    :returns: Tuple with boolean on whether the app needs to be updated and the version it was
    compared to. This version is the update version if the ``True`` and it's ``None`` if there's
    no manifest file for the update.

    :raises FileNotFoundError: If the update manifest file doesn't exist.
    """
    update_manifest = update_manifest or config.update_manifest

    if not update_manifest:
        return False, None

    update_manifest_dict = config.read_manifest_file(update_manifest)
    new_app_version = Version(update_manifest_dict['version'])

    return config.version < new_app_version, new_app_version


def perform_update(update_file=None):
    if not config.IS_BUNDLED_APP:
        raise Exception('Update only works when running the bundled (executable) app.')

    update_file = update_file or config.update_file
    shutil.copy(update_file, sys.executable)


if __name__ == '__main__':
    import logging
    import time
    from argparse import ArgumentParser, RawTextHelpFormatter
    from pathlib import Path

    description = f'App updater.'

    parser = ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        '--current-file',
        type=str,
        help='Path to existing file to be updated.',
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

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.getLevelName(args.log_level.upper()),
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    current_file = Path(args.current_file).resolve()
    update_file = Path(args.update_file).resolve()
    logging.info(f'Updating app.\n  Current file: {current_file}\n  Update file: {update_file}')

    success = False
    while (tries := 5) > 0:
        try:
            shutil.copy(args.update_file, args.current_file)
            success = True
            break
        except shutil.SameFileError as e:
            # Process still in use. Try again.
            logging.warning(f'Failed to update. Trying again.\n{e}')
            time.sleep(0.5)
            tries -= 1

    if not success:
        logging.error('Unable to update.')
        sys.exit(1)
    logging.info('Update successful.')
