from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# Need one (and only one) `QApplication` instance per application.
# Pass in `sys.argv` to allow command line arguments for the app.
# If command line arguments re not used, `QApplication([])` works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # Windows are hidden by default.

# Start the event loop.
app.exec()

# Application won't reach here until you exit and the event loop has stopped.
