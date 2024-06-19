import sys
from pathlib import Path

import yaml
from semantic_version import Version


def read_manifest_file(manifest) -> dict:
    with open(manifest) as f:
        return yaml.safe_load(f)


IS_BUNDLED_APP = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
"""
Whether the code is running as an executable bundled by PyInstaller or as normal Python code.

More info at https://pyinstaller.org/en/stable/runtime-information.html
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

no_check_update = False
check_update_only = False
update_manifest = None
update_file = None
