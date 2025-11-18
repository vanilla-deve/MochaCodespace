from pathlib import Path
import sys

from qt_compat import QApplication, USING_PYQT

# Ensure Python path includes project root so relative imports work when running main.py directly
ROOT = Path(__file__).parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ui.app_window import MochaCodespace

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MochaCodespace()
    window.show()

    # Different exec name for PyQt6/PySide6 compatibility
    sys.exit(app.exec() if USING_PYQT else app.exec())

if __name__ == "__main__":
    main()
