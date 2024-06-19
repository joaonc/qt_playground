import os
import sys

from semantic_version import Version

import src.config as config


def check_update(update_manifest=None) -> tuple[bool, Version]:
    """
    Check if there's a newer version of the app.

    :param update_manifest: The new app's  manifest file location.
    :return:
    """
    update_manifest = update_manifest or config.update_manifest
    new_app = config.read_manifest_file(update_manifest)
    new_app_version = Version(new_app['version'])
    return config.version < new_app_version, new_app_version


def perform_update(file):
    # Get current working directory
    cwd = os.getcwd()
    # Get the path of the currently running script
    script_path = os.path.realpath(sys.argv[0])
