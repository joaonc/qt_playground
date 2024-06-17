Tests use [pytest](https://pytest.org/) and the
[pytest-qt](https://github.com/pytest-dev/pytest-qt) plugin (documentation
[here](https://pytest-qt.readthedocs.io/en/latest/)).

Also see the [QTest API](https://doc.qt.io/qt-6/qtest.html) for more info.

These test the UI by simulating user interaction.

`pytest-qt` supplies the [`qtbot`](https://pytest-qt.readthedocs.io/en/latest/reference.html#module-pytestqt.qtbot)
fixture, which is not required to be used, but keeps track of the widget and will ensure that it
gets closed by the end of the test, so it is highly recommended.
