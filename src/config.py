import os
import sys
from pathlib import Path

import yaml
from semantic_version import Version


def read_manifest_file(manifest) -> dict:
    with open(manifest) as f:
        return yaml.safe_load(f)


def is_truthy(value) -> bool:
    return str(value).strip().lower() in ['true', '1']


IS_BUNDLED_APP = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
"""
Whether the code is running as an executable bundled by PyInstaller or as normal Python code.

More info at https://pyinstaller.org/en/stable/runtime-information.html
"""

IGNORE_BUNDLED_APP = is_truthy(os.environ.get('QT_PLAYGROUND_IGNORE_BUNDLED_APP', 'False'))
"""
Ignore ``IS_BUNDLED_APP``, ie, code that is supposed to execute only as a bundled app can run as
script also.

To be used for debugging purposes.

Set the environment variable ``QT_PLAYGROUND_IGNORE_BUNDLED_APP`` to ``True`` or ``1`` when
executing the code as a script. Ignored when running as a bundled app.
"""

IGNORE_UPDATE = is_truthy(os.environ.get('QT_PLAYGROUND_IGNORE_UPDATE', 'False'))
"""
Do not perform an app update (and backup), even if one is available.

See also the ``check-update`` and ``check-update-only`` CLI options.

To be used for debugging purposes.

Set the environment variable ``QT_PLAYGROUND_IGNORE_UPDATE`` to ``True`` or ``1``.
"""

if IS_BUNDLED_APP:
    PROJECT_ROOT = Path(sys._MEIPASS)  # noqa
else:
    PROJECT_ROOT = Path(__file__).parents[1]

ASSETS_DIR = PROJECT_ROOT / 'assets'
APP_MANIFEST_FILE = ASSETS_DIR / 'app.yaml'

app_manifest = read_manifest_file(APP_MANIFEST_FILE)

version = Version(app_manifest['version'])
"""App version."""

check_update = True
"""Check for app updates."""
check_update_only = False
"""Only check for updates and do not launch the app."""
update_manifest = None
update_file = None
backup_file = None
