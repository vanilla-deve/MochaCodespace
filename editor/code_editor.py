import re
from qt_compat import (
    QPlainTextEdit, QFont, QCompleter, Qt, QStringListModel, QTextCursor
)
from .highlighter import SyntaxHighlighter
from config.keywords import LANGUAGE_KEYWORDS

class CodeEditor(QPlainTextEdit):
    """Enhanced code editor with syntax highlighting and autocompletion"""

    def __init__(self, parent=None, language="Python"):
        super().__init__(parent)
        self.language = language
        self.setup_editor()
        self.setup_autocomplete()
        self.highlighter = SyntaxHighlighter(self.document(), language)

    def setup_editor(self):
        font = QFont("JetBrains Mono", 11)
        if not font.exactMatch():
            font = QFont("Fira Code", 11)
        if not font.exactMatch():
            font = QFont("Consolas", 11)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.setFont(font)
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #f5ebe0;
                color: #704241;
                selection-background-color: #e3d5ca;
                border: none;
                padding: 8px;
            }
        """)
        self.setTabStopDistance(self.fontMetrics().horizontalAdvance(' ') * 4)

    def setup_autocomplete(self):
        self.completer = QCompleter()
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        self.completer.popup().setStyleSheet("""
            QListView {
                background-color: #f5ebe0;
                color: #704241;
                border: 2px solid #d5bdaf;
                border-radius: 6px;
                padding: 4px;
                font-family: 'JetBrains Mono', 'Consolas', monospace;
                selection-background-color: #e3d5ca;
            }
        """)
        self.completer.activated.connect(self.insert_completion)
        self.update_completer_model()

    def update_completer_model(self):
        keywords = LANGUAGE_KEYWORDS.get(self.language, [])
        text = self.toPlainText()
        words = set(re.findall(r'\b[A-Za-z_][A-Za-z0-9_]{2,}\b', text))
        all_completions = sorted(set(keywords) | words)
        model = QStringListModel(all_completions)
        self.completer.setModel(model)

    def insert_completion(self, completion):
        cursor = self.textCursor()
        prefix = self.completer.completionPrefix()
        if prefix:
            # Replace the current prefix with completion
            for _ in range(len(prefix)):
                cursor.deletePreviousChar()
        cursor.insertText(completion)
        self.setTextCursor(cursor)

    def text_under_cursor(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.SelectionType.WordUnderCursor)
        return cursor.selectedText()

    def keyPressEvent(self, event):
        # If completer popup is visible, let it handle navigation keys
        if self.completer.popup().isVisible():
            if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return,
                               Qt.Key.Key_Escape, Qt.Key.Key_Tab, Qt.Key.Key_Backtab):
                event.ignore()
                return

        # Auto-indent
        if event.key() == Qt.Key.Key_Return:
            cursor = self.textCursor()
            block = cursor.block()
            text = block.text()
            indent = len(text) - len(text.lstrip())
            stripped = text.rstrip()
            if stripped.endswith((':', '{', '(')):
                indent += 4
            super().keyPressEvent(event)
            self.insertPlainText(' ' * indent)
            return

        # Tab inserts 4 spaces
        if event.key() == Qt.Key.Key_Tab:
            self.insertPlainText(' ' * 4)
            return

        super().keyPressEvent(event)

        # Show completer when appropriate
        completion_prefix = self.text_under_cursor()
        if event.key() == Qt.Key.Key_Space and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.update_completer_model()
            self.completer.setCompletionPrefix("")
            rect = self.cursorRect()
            self.completer.complete(rect)
        elif len(completion_prefix) >= 2 and event.text().isalnum():
            self.update_completer_model()
            self.completer.setCompletionPrefix(completion_prefix)
            if self.completer.completionCount() > 0:
                rect = self.cursorRect()
                self.completer.complete(rect)

    def set_language(self, language):
        self.language = language
        self.highlighter.set_language(language)
        self.update_completer_model()
