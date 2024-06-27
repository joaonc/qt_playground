from src.ui.playground_main_window import PlaygroundMainWindow


def test_enter_text(qtbot):
    widget = PlaygroundMainWindow()
    qtbot.addWidget(widget)

    widget.input_line_edit.setText('Foo')
    widget.message_button.click()

    text = widget.output_plain_text_edit.toPlainText()
    assert text == 'Foo'
