from pathlib import Path
from qt_compat import QVBoxLayout, QWidget, QLabel, QMessageBox
from .code_editor import CodeEditor
from config.samples import SAMPLE_CODE

class EditorTab(QWidget):
    """Individual editor tab"""

    def __init__(self, language="Python", filepath=None):
        super().__init__()
        self.language = language
        self.filepath = Path(filepath) if filepath else None
        self.setup_ui()
        self.load_content()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.editor = CodeEditor(language=self.language)
        layout.addWidget(self.editor)

    def load_content(self):
        if self.filepath and self.filepath.exists():
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.editor.setPlainText(f.read())
        else:
            self.editor.setPlainText(SAMPLE_CODE.get(self.language, ""))

    def get_content(self):
        return self.editor.toPlainText()

    def save(self, filepath=None):
        if filepath:
            self.filepath = Path(filepath)
        if not self.filepath:
            return False
        # Ensure extension
        # Language config is used by app_window when saving to propose extension; here keep simple
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write(self.get_content())
            return True
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Failed to save file:\n{str(e)}")
            return False
