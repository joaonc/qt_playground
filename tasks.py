import os
from pathlib import Path

from invoke import Collection, Exit, task

os.environ.setdefault('INVOKE_RUN_ECHO', '1')  # Show commands by default


PROJECT_ROOT = Path(__file__).parent
ASSETS_DIR = PROJECT_ROOT / 'assets'

# Requirements files
REQUIREMENTS_MAIN = 'main'
REQUIREMENTS_FILES = {
    REQUIREMENTS_MAIN: 'requirements',
    'dev': 'requirements-dev',
    'docs': 'requirements-docs',
}
"""
Requirements files.
Order matters as most operations with multiple files need ``requirements.txt`` to be processed
first.
Add new requirements files here.
"""

REQUIREMENTS_TASK_HELP = {
    'requirements': '`.in` file. Full name not required, just the initial name after the dash '
    f'(ex. "dev"). For main file use "{REQUIREMENTS_MAIN}". Available requirements: '
    f'{", ".join(REQUIREMENTS_FILES)}.'
}

UI_FILES = tuple((ASSETS_DIR / 'ui').glob("**/*.ui"))
"""
QT ``.ui`` files.
"""

BUILD_IN_FILE = PROJECT_ROOT / 'src' / 'main.py'
BUILD_WORK_DIR = PROJECT_ROOT / 'build'
BUILD_DIST_DIR = PROJECT_ROOT / 'dist'


def _csstr_to_list(csstr: str) -> list[str]:
    """
    Convert a comma-separated string to list.
    """
    return [s.strip() for s in csstr.split(',')]


def _get_requirements_file(requirements: str, extension: str) -> str:
    """
    Return the full requirements file name (with extension).

    :param requirements: The requirements file to retrieve. Can be the whole filename
        (no extension), ex `'requirements-dev'` or just the initial portion, ex `'dev'`.
        Use `'main'` for the `requirements` file.
    :param extension: Requirements file extension. Can be either `'in'` or `'txt'`.
    """
    filename = REQUIREMENTS_FILES.get(requirements, requirements)
    if filename not in REQUIREMENTS_FILES.values():
        raise Exit(f'`{requirements}` is an unknown requirements file.')

    return f'{filename}.{extension.lstrip(".")}'


def _get_requirements_files(requirements: str | None, extension: str) -> list[str]:
    extension = extension.lstrip('.')
    if requirements is None:
        requirements_files = list(REQUIREMENTS_FILES)
    else:
        requirements_files = _csstr_to_list(requirements)

    # Get full filename+extension and sort by the order defined in `REQUIREMENTS_FILES`
    filenames = [
        _get_requirements_file(r, extension) for r in REQUIREMENTS_FILES if r in requirements_files
    ]

    return filenames


@task
def build_clean(c):
    """
    Delete files created from previous builds (`build` and `dist` folders).
    """
    import shutil

    for d in [BUILD_WORK_DIR, BUILD_DIST_DIR]:
        shutil.rmtree(d, ignore_errors=True)


@task(build_clean)
def build_dist(c):
    """
    Build the distributable/executable file(s).
    """
    c.run(
        f'pyinstaller '
        f'--onefile "{BUILD_IN_FILE}" --distpath "{BUILD_DIST_DIR}" --workpath "{BUILD_WORK_DIR}" '
        f'--specpath "{BUILD_WORK_DIR}"'
    )


@task
def build_run(c):
    """
    Run the built package.
    """
    import platform

    if platform.system() == 'Windows':
        exes = list(BUILD_DIST_DIR.glob('**/*.exe'))
        if len(exes) == 0:
            raise Exit('No executable found.')
        elif len(exes) > 1:
            raise Exit('Multiple executables found.')
        c.run(str(exes[0]))
    elif platform.system() == 'Darwin':
        raise Exit('Running on MacOS still needs to be implemented.')
    else:
        raise Exit(f'Running on {platform.system()} is not supported.')


@task(
    help={
        'file': '`.ui` file to be converted to `.py`. `.ui` extension not required. Can be a comma '
        'separated. If not supplied, all files will be converted. Available files: '
        f'{", ".join(p.stem for p in UI_FILES)}.'
    }
)
def ui_py(c, file=None):
    """
    Convert QT `.ui` files into `.py`.
    """
    if file:
        file_stems = [
            (_f2[:-3] if _f2.lower().endswith('.ui') else _f2)
            for _f2 in [_f1.strip() for _f1 in file.split(',')]
        ]
    else:
        file_stems = [p.stem for p in UI_FILES]

    for file_stem in file_stems:
        ui_file_path = next((p for p in UI_FILES if p.stem == file_stem), None)
        if not ui_file_path:
            raise Exit(
                f'File "{file}" not found. Available files: {", ".join(p.stem for p in UI_FILES)}'
            )

        py_file_path = PROJECT_ROOT / 'src/ui/forms' / f'ui_{file_stem}.py'

        c.run(f'pyside6-uic {ui_file_path} -o {py_file_path}')


@task(
    help={
        'file': f'`.ui` file to be edited. Available files: {", ".join(p.stem for p in UI_FILES)}.'
    }
)
def ui_edit(c, file):
    """
    Edit a file in QT Designer.
    """
    file_stem = file[:-3] if file.lower().endswith('.ui') else file
    ui_file_path = next((p for p in UI_FILES if p.stem == file_stem), None)
    if not ui_file_path:
        raise Exit(
            f'File "{file}" not found. Available files: {", ".join(p.stem for p in UI_FILES)}'
        )

    c.run(f'pyside6-designer {ui_file_path}', asynchronous=True)


@task
def lint_black(c, path='.'):
    c.run(f'black {path}')


@task
def lint_flake8(c, path='.'):
    c.run(f'flake8 {path}')


@task
def lint_isort(c, path='.'):
    c.run(f'isort {path}')


@task
def lint_mypy(c, path='.'):
    c.run(f'mypy {path}')


@task(lint_isort, lint_black, lint_flake8, lint_mypy)
def lint_all(c):
    """
    Run all linters.
    Config for each of the tools is in ``pyproject.toml`` and ``setup.cfg``.
    """
    print('Done')


@task
def test_unit(c):
    """
    Runs unit tests that check functionality in this project's helper libraries.
    """
    c.run('python -m pytest tests/tests/unit')


@task(help=REQUIREMENTS_TASK_HELP)
def pip_compile(c, requirements=None):
    """
    Compile requirements file(s).
    """
    for filename in _get_requirements_files(requirements, 'in'):
        c.run(f'pip-compile {filename}')


@task(help=REQUIREMENTS_TASK_HELP)
def pip_sync(c, requirements=None):
    """
    Synchronize environment with requirements file.
    """
    c.run(f'pip-sync {" ".join(_get_requirements_files(requirements, "txt"))}')


@task(
    help=REQUIREMENTS_TASK_HELP | {'package': 'Package to upgrade. Can be a comma separated list.'}
)
def pip_package(c, requirements, package):
    """
    Upgrade package.
    """
    packages = [p.strip() for p in package.split(',')]
    for filename in _get_requirements_files(requirements, 'in'):
        c.run(f'pip-compile --upgrade-package {" --upgrade-package ".join(packages)} {filename}')


@task(help=REQUIREMENTS_TASK_HELP)
def pip_upgrade(c, requirements):
    """
    Try to upgrade all dependencies to their latest versions.
    """
    for filename in _get_requirements_files(requirements, 'in'):
        c.run(f'pip-compile --upgrade {filename}')


@task
def precommit_install(c):
    """
    Install pre-commit into the git hooks, which will cause pre-commit to run on automatically.
    This should be the first thing to do after cloning this project and installing requirements.
    """
    c.run('pre-commit install')


@task
# `upgrade` instead of `update` to maintain similar naming to `pip-compile upgrade`
def precommit_upgrade(c):
    """
    Upgrade pre-commit config to the latest repos' versions.
    """
    c.run('pre-commit autoupdate')


@task(help={'hook': 'Name of hook to run. Default is to run all.'})
def precommit_run(c, hook=None):
    """
    Manually run pre-commit hooks.
    """
    hook = hook or '--all-files'
    c.run(f'pre-commit run {hook}')


@task
def docs_serve(c):
    """
    Start documentation local server.
    """
    c.run('mkdocs serve')


@task
def docs_deploy(c):
    """
    Publish documentation to GitHub Pages at https://xealenergy.github.io/xeal-nift-qa
    """
    c.run('mkdocs gh-deploy')


ns = Collection()  # Main namespace

test_collection = Collection('test')
test_collection.add_task(test_unit, 'unit')

build_collection = Collection('build')
build_collection.add_task(build_clean, 'clean')
build_collection.add_task(build_dist, 'dist')
build_collection.add_task(build_run, 'run')

lint_collection = Collection('lint')
lint_collection.add_task(lint_all, 'all')
lint_collection.add_task(lint_black, 'black')
lint_collection.add_task(lint_flake8, 'flake8')
lint_collection.add_task(lint_isort, 'isort')
lint_collection.add_task(lint_mypy, 'mypy')

pip_collection = Collection('pip')
pip_collection.add_task(pip_compile, 'compile')
pip_collection.add_task(pip_package, 'package')
pip_collection.add_task(pip_sync, 'sync')
pip_collection.add_task(pip_upgrade, 'upgrade')

precommit_collection = Collection('precommit')
precommit_collection.add_task(precommit_run, 'run')
precommit_collection.add_task(precommit_install, 'install')
precommit_collection.add_task(precommit_upgrade, 'upgrade')

docs_collection = Collection('docs')
docs_collection.add_task(docs_serve, 'serve')
docs_collection.add_task(docs_deploy, 'deploy')

ui_collection = Collection('ui')
ui_collection.add_task(ui_py, 'py')
ui_collection.add_task(ui_edit, 'edit')

ns.add_collection(build_collection)
ns.add_collection(lint_collection)
ns.add_collection(pip_collection)
ns.add_collection(precommit_collection)
ns.add_collection(test_collection)
ns.add_collection(docs_collection)
ns.add_collection(ui_collection)
