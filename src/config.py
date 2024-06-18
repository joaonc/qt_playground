import yaml
import semantic_version
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[1]
ASSETS_DIR = PROJECT_ROOT / 'assets'
APP_MANIFEST_FILE = ASSETS_DIR / 'app.yaml'

with APP_MANIFEST_FILE.open() as f:
    app_manifest = yaml.safe_load(f)

version = semantic_version.Version(app_manifest['version'])
