# Qt Playground
Playing around with **Qt** for learning purposes.

Uses [Qt 6](https://www.qt.io) and [Qt for Python](https://wiki.qt.io/Qt_for_Python), aka _PySide_,
which includes _Qt Designer_, a WYSIWYG UI editor.

## Getting started
### Requirements
```
pip install -r requirements-dev.txt
```

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

## Resources
* [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
* [First steps with Qt Designer](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)