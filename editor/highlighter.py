import re
from qt_compat import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

from config.keywords import LANGUAGE_KEYWORDS

class SyntaxHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for multiple languages"""
    def __init__(self, parent, language="Python"):
        super().__init__(parent)
        self.language = language
        self.setup_rules()

    def setup_rules(self):
        self.rules = []

        # Colors (Mocha-ish)
        keyword_color = QColor("#8b4513")
        string_color = QColor("#6b8e23")
        comment_color = QColor("#a0826d")
        number_color = QColor("#cd853f")
        function_color = QColor("#704241")

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(keyword_color)
        keyword_format.setFontWeight(QFont.Weight.Bold)

        keywords = LANGUAGE_KEYWORDS.get(self.language, [])
        for word in keywords:
            pattern = rf"\b{re.escape(word)}\b"
            self.rules.append((re.compile(pattern), keyword_format))

        string_format = QTextCharFormat()
        string_format.setForeground(string_color)
        self.rules.append((re.compile(r'"[^"\\]*(\\.[^"\\]*)*"'), string_format))
        self.rules.append((re.compile(r"'[^'\\]*(\\.[^'\\]*)*'"), string_format))

        number_format = QTextCharFormat()
        number_format.setForeground(number_color)
        self.rules.append((re.compile(r'\b\d+\.?\d*\b'), number_format))

        function_format = QTextCharFormat()
        function_format.setForeground(function_color)
        function_format.setFontItalic(True)
        self.rules.append((re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*(?=\()'), function_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(comment_color)
        comment_format.setFontItalic(True)

        if self.language in ["Python", "Ruby", "Nix"]:
            self.rules.append((re.compile(r'#[^\n]*'), comment_format))
        elif self.language == "Lua":
            self.rules.append((re.compile(r'--[^\n]*'), comment_format))
        elif self.language in ["C", "C++", "Java", "JavaScript", "TypeScript",
                               "Rust", "Go", "C#", "Kotlin"]:
            self.rules.append((re.compile(r'//[^\n]*'), comment_format))
            self.rules.append((re.compile(r'/\*.*?\*/', re.DOTALL), comment_format))
        elif self.language == "HTML":
            self.rules.append((re.compile(r'<!--.*?-->', re.DOTALL), comment_format))
        elif self.language == "CSS":
            self.rules.append((re.compile(r'/\*.*?\*/', re.DOTALL), comment_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            for m in pattern.finditer(text):
                start = m.start()
                length = m.end() - start
                self.setFormat(start, length, fmt)

    def set_language(self, language):
        self.language = language
        self.setup_rules()
        self.rehighlight()
