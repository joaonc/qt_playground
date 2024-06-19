import shutil
import logging
import os
import sys
from pathlib import Path

from semantic_version import Version

import src.config as config


def check_update(update_manifest=None) -> tuple[bool, Version]:
    """
    Check if there's a newer version of the app.

    :param update_manifest: The new app's  manifest file location.
    :return:
    """
    update_manifest = update_manifest or config.update_manifest
    update_manifest_dict = config.read_manifest_file(update_manifest)
    new_app_version = Version(update_manifest_dict['version'])

    return config.version < new_app_version, new_app_version


def perform_update(update_file=None):
    if not config.IS_BUNDLED_APP:
        raise Exception('Update only works when running the bundled (executable) app.')

    update_file = update_file or config.update_file
    shutil.copy(update_file, sys.executable)
