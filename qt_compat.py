import sys

try:
    # PyQt6
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QTextEdit, QPlainTextEdit, QPushButton, QLabel, QComboBox,
        QFileDialog, QMessageBox, QInputDialog, QSplitter, QTreeWidget,
        QTreeWidgetItem, QTabWidget, QToolBar, QStatusBar, QMenuBar, QMenu,
        QCompleter, QListWidget
    )
    from PyQt6.QtCore import Qt, QTimer, pyqtSignal as Signal, QThread, QStringListModel, QRect
    from PyQt6.QtGui import (QFont, QTextCharFormat, QColor, QTextCursor, QKeySequence,
                             QAction, QSyntaxHighlighter, QPalette)
    USING_PYQT = True
except Exception:
    # PySide6 fallback
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QTextEdit, QPlainTextEdit, QPushButton, QLabel, QComboBox,
        QFileDialog, QMessageBox, QInputDialog, QSplitter, QTreeWidget,
        QTreeWidgetItem, QTabWidget, QToolBar, QStatusBar, QMenuBar, QMenu,
        QCompleter, QListWidget
    )
    from PySide6.QtCore import Qt, QTimer, Signal, QThread, QStringListModel, QRect
    from PySide6.QtGui import (QFont, QTextCharFormat, QColor, QTextCursor, QKeySequence,
                               QAction, QSyntaxHighlighter, QPalette)
    USING_PYQT = False

# Exported names: modules can import like `from qt_compat import QApplication, Qt, QThread, ...`
__all__ = [
    "QApplication", "QMainWindow", "QWidget", "QVBoxLayout", "QHBoxLayout",
    "QTextEdit", "QPlainTextEdit", "QPushButton", "QLabel", "QComboBox",
    "QFileDialog", "QMessageBox", "QInputDialog", "QSplitter", "QTreeWidget",
    "QTreeWidgetItem", "QTabWidget", "QToolBar", "QStatusBar", "QMenuBar", "QMenu",
    "QCompleter", "QListWidget", "Qt", "QTimer", "Signal", "QThread", "QStringListModel",
    "QRect", "QFont", "QTextCharFormat", "QColor", "QTextCursor", "QKeySequence",
    "QAction", "QSyntaxHighlighter", "QPalette", "USING_PYQT"
]
