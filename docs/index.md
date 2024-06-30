# Qt Playground
Playing around with **Qt** for learning purposes.

Uses [Qt 6](https://www.qt.io) and [Qt for Python](https://wiki.qt.io/Qt_for_Python), aka _PySide_,
which includes _Qt Designer_, a WYSIWYG UI editor.

## Getting started
### Requirements
```
pip install -r requirements-dev.txt
```

!!! Note

    If running tests (which uses `pytest`) on Python `<= 3.10`, then the `exceptiongroup` package
    needs to be installed.

    This can be done with:
    ```
    pip install -U pytest
    ```

    This will force upgrade `pytest`, which will install any dependencies not yet installed (ex.
    `exceptiongroup`).  
    This dependency is not in `requirements-dev.txt` because this file is generated with Python
    3.11+.

## Development
### UI
`Qt Designer` is used to create the UI, which outputs a `.ui` file (XML content that describes the
UI). This file is then transformed into a `.py` file.

All the required tools are available by installing `pyside6`:

* `Qt Designer`: `pyside6-designer`
* `.ui > .py` Converter: `pyside6-uic`
  At the project root (use full paths if relative doesn't work):
  ```
  pyside6-uic assets/ui/settings.ui -o hd_active/ui/forms/settings_ui.py
  ```

#### Edit UI file
```
inv ui.edit <file>

ex:
  * inv ui.edit app.ui
  * inv ui.edit app  # extension not required
```

#### Convert `.ui` to `.py`
```
inv ui.py <file>  # `.ui` extension not required

# Can be multiple files, comma separated
inv ui.py <file1>,<file2>
```

### IDE
In most cases, the code editor used will be [VS Code](https://code.visualstudio.com/) or
[PyCharm](https://www.jetbrains.com/pycharm/).

In this case, PyCharm was used and some of its features are seen in the code in the form of
comments that add functionality:

* `# noinspection`  
  PyCharm's internal linter and rule inspector checks for things that the linters used (`flake8`,
  `mypy`, etc.) may not check and a warning appears in the IDE. That warning can be disabled with
  the `# noinspection <inspection_name>` directive.
* `# region`  
  The `# region <region_name>` / `# endregion` directives create a foldable block of code that makes
  it easier to identify what that block is doing and hiding it when reading the code at a higher
  level.

## Qt Installation
https://doc.qt.io/qt-6/get-and-install-qt.html

For this project, installed the single developer open source (free) version.

In the _custom setup_ section, there's a _Qt Installation Framework_ that is unchecked by default.
Checked that box  to install that component, but at this point it's unclear whether that's
necessary (still learning how to install a Qt app).

See [this video](https://www.youtube.com/watch?v=1pKMcwJZay4) for more details.

Takes a while to download and install.
