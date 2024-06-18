from pathlib import Path

import sys
import yaml
from semantic_version import Version

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

with open(APP_MANIFEST_FILE) as f:
    app_manifest = yaml.safe_load(f)

version = Version(app_manifest['version'])
"""App version."""

no_check_update = False
check_update_only = False
update_manifest = Path('app.yaml')
update_file = Path('qt_playground.exe')
