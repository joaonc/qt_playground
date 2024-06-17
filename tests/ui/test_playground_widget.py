from src.ui.playground_widget import PlaygroundWidget


def test_enter_text(qtbot):
    widget = PlaygroundWidget()
    qtbot.addWidget(widget)

    widget.input_line_edit.setText('Foo')
    widget.message_button.click()

    text = widget.output_plain_text_edit.toPlainText()
    assert text == 'Foo'
