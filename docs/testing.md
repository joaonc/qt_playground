Tests use [pytest](https://pytest.org/) and the
[pytest-qt](https://github.com/pytest-dev/pytest-qt) plugin (documentation
[here](https://pytest-qt.readthedocs.io/en/latest/)).

Also see the [QTest API](https://doc.qt.io/qt-6/qtest.html) for more info.

These test the UI by simulating user interaction.

`pytest-qt` supplies the [`qtbot`](https://pytest-qt.readthedocs.io/en/latest/reference.html#module-pytestqt.qtbot)
fixture, which is not required to be used, but keeps track of the widget and will ensure that it
gets closed by the end of the test, so it is highly recommended.

## Running the unit tests
If using an IDE such as PyCharm or VS Code, the tests can be executed from within the IDE.

To run via CLI:
```
pytest .
```
or
```
python -m pytest .
```

Pytest options are in `pyproject.toml`, in the `[tool.pytest.ini_options]` section.

## Testing app update
TODO: More instructions here.
```
.\dist\qt_playground.exe --check-update-only --log-level debug --update-manifest "./dist_test/app.yaml" --update-file "./dist_test/qt_playground_101.exe"
```
