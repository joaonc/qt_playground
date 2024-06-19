# -*- mode: python ; coding: utf-8 -*-

# Spec file for PyInstaller.
# This is executable Python code. PyInstaller builds the app by executing the contents of this file.
# https://pyinstaller.org/en/stable/spec-files.html

from pathlib import Path

PROJECT_ROOT = Path(SPECPATH).parent.resolve(strict=True)
SOURCE_DIR = PROJECT_ROOT / 'src'
ASSETS_DIR = PROJECT_ROOT / 'assets'
APP_MANIFEST_FILE = ASSETS_DIR / 'app.yaml'


a = Analysis(
    [str(SOURCE_DIR / 'main.py')],
    pathex=[],
    binaries=[],
    # https://pyinstaller.org/en/stable/spec-files.html#adding-data-files
    datas=[(str(APP_MANIFEST_FILE), str(ASSETS_DIR.relative_to(PROJECT_ROOT)))],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

# onefile
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='qt_playground',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
