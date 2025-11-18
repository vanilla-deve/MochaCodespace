LANGUAGE_KEYWORDS = {
    "Python": [
        "and", "as", "assert", "async", "await", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "False", "finally", "for",
        "from", "global", "if", "import", "in", "is", "lambda", "None",
        "nonlocal", "not", "or", "pass", "raise", "return", "True", "try",
        "while", "with", "yield", "print", "len", "range", "str", "int",
        "float", "list", "dict", "set", "tuple", "open", "self", "__init__"
    ],
    "Java": [
        "abstract", "assert", "boolean", "break", "byte", "case", "catch",
        "char", "class", "const", "continue", "default", "do", "double",
        "else", "enum", "extends", "final", "finally", "float", "for",
        "if", "implements", "import", "instanceof", "int", "interface",
        "long", "native", "new", "package", "private", "protected", "public",
        "return", "short", "static", "strictfp", "super", "switch", "synchronized",
        "this", "throw", "throws", "transient", "try", "void", "volatile", "while",
        "String", "System", "out", "println", "main", "args"
    ],
    "C": [
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if",
        "int", "long", "register", "return", "short", "signed", "sizeof",
        "static", "struct", "switch", "typedef", "union", "unsigned", "void",
        "volatile", "while", "printf", "scanf", "malloc", "free", "NULL",
        "include", "define", "stdio", "stdlib", "string"
    ],
    "C++": [
        "alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand", "bitor",
        "bool", "break", "case", "catch", "char", "class", "const", "constexpr",
        "continue", "decltype", "default", "delete", "do", "double", "dynamic_cast",
        "else", "enum", "explicit", "export", "extern", "false", "float", "for",
        "friend", "goto", "if", "inline", "int", "long", "mutable", "namespace",
        "new", "noexcept", "not", "nullptr", "operator", "or", "private", "protected",
        "public", "return", "short", "signed", "sizeof", "static", "struct", "switch",
        "template", "this", "throw", "true", "try", "typedef", "typeid", "typename",
        "union", "unsigned", "using", "virtual", "void", "volatile", "while",
        "cout", "cin", "endl", "string", "vector", "iostream", "std"
    ],
    "JavaScript": [
        "async", "await", "break", "case", "catch", "class", "const", "continue",
        "debugger", "default", "delete", "do", "else", "export", "extends", "false",
        "finally", "for", "function", "if", "import", "in", "instanceof", "let",
        "new", "null", "return", "super", "switch", "this", "throw", "true",
        "try", "typeof", "var", "void", "while", "with", "yield",
        "console", "log", "document", "window", "Array", "Object", "String",
        "Number", "Boolean", "Math", "Date", "JSON", "Promise", "setTimeout"
    ],
    "TypeScript": [
        "abstract", "any", "as", "async", "await", "boolean", "break", "case",
        "catch", "class", "const", "continue", "debugger", "declare", "default",
        "delete", "do", "else", "enum", "export", "extends", "false", "finally",
        "for", "from", "function", "if", "implements", "import", "in", "instanceof",
        "interface", "is", "keyof", "let", "module", "namespace", "never", "new",
        "null", "number", "of", "package", "private", "protected", "public",
        "readonly", "require", "return", "static", "string", "super", "switch",
        "symbol", "this", "throw", "true", "try", "type", "typeof", "undefined",
        "unique", "unknown", "var", "void", "while", "with", "yield"
    ],
    "Rust": [
        "as", "async", "await", "break", "const", "continue", "crate", "dyn",
        "else", "enum", "extern", "false", "fn", "for", "if", "impl", "in",
        "let", "loop", "match", "mod", "move", "mut", "pub", "ref", "return",
        "self", "Self", "static", "struct", "super", "trait", "true", "type",
        "unsafe", "use", "where", "while", "String", "Vec", "Option", "Result",
        "println", "print", "format", "panic", "unwrap", "expect"
    ],
    "Go": [
        "break", "case", "chan", "const", "continue", "default", "defer", "else",
        "fallthrough", "for", "func", "go", "goto", "if", "import", "interface",
        "map", "package", "range", "return", "select", "struct", "switch", "type",
        "var", "fmt", "Println", "Printf", "Sprintf", "main", "string", "int",
        "bool", "float64", "error", "nil", "true", "false", "make", "len", "append"
    ],
    "Ruby": [
        "alias", "and", "begin", "break", "case", "class", "def", "defined",
        "do", "else", "elsif", "end", "ensure", "false", "for", "if", "in",
        "module", "next", "nil", "not", "or", "redo", "rescue", "retry",
        "return", "self", "super", "then", "true", "undef", "unless", "until",
        "when", "while", "yield", "puts", "print", "gets", "attr_accessor",
        "attr_reader", "attr_writer", "initialize", "new", "require"
    ],
    "HTML": [
        "html", "head", "title", "body", "div", "span", "p", "a", "img",
        "ul", "ol", "li", "table", "tr", "td", "th", "form", "input",
        "button", "select", "option", "textarea", "label", "h1", "h2",
        "h3", "h4", "h5", "h6", "header", "footer", "nav", "section",
        "article", "aside", "main", "script", "style", "link", "meta",
        "br", "hr", "strong", "em", "code", "pre"
    ],
    "CSS": [
        "color", "background", "background-color", "font-family", "font-size",
        "font-weight", "margin", "padding", "border", "width", "height",
        "display", "position", "top", "left", "right", "bottom", "flex",
        "grid", "justify-content", "align-items", "text-align", "cursor",
        "transition", "transform", "opacity", "z-index", "overflow", "box-shadow"
    ],
    "PTX": [
        "AL2P", "ALD", "AST", "B2R", "BFE", "BFI", "BMMA", "BMOV", "BMSK", "BREV",
        "BRK", "CCTL", "CCTLL", "CCTLT", "CONT", "CS2R", "CSET", "CSETP", "DADD",
        "DEPBAR", "DFMA", "DMMA", "DMNMX", "DMUL", "DSET", "DSETP", "F2F", "F2FP",
        "F2I", "F2IP", "FADD", "FADD32I", "FCHK", "FCMP", "FFMA", "FFMA32I", "FLO",
        "FMNMX", "FMUL", "FMUL32I", "FRND", "FSEL", "FSET", "FSETP", "FSWZADD",
        "GETCRSPTR", "GETLMEMBASE", "HADD2", "HFMA2", "HMMA", "HMNMX2", "HMUL2",
        "HSET2", "HSETP2", "I2F", "I2FP", "I2I", "I2IP", "IABS", "IADD", "IADD3",
        "IADD32I", "ICMP", "IDE", "IDP", "IMAD", "IMAD32I", "IMADSP", "IMMA", "IMNMX",
        "IMUL", "IMUL32I", "IPA", "ISBERD", "ISBEWR", "ISCADD", "ISCADD32I", "ISET", "ISETP",
        "JCAL", "LDC", "LDGDEPBAR", "LDGSTS", "LEA", "LEPC", "LONGJMP", "LOP", "LOP3",
        "LOP32I", "MATCH", "MOV", "MOV32I", "MOVM", "MUFU", "NOP", "OUT", "P2R", "PCNT",
        "PEXIT", "PIXLD", "PLONGJMP", "PLOP3", "POPC", "PRMT", "PSET", "PSETP", "QSPC",
        "R2B", "R2P", "R2UR", "RAM", "REDUX", "RRO", "RTT", "S2R", "S2UR", "SAM", "SEL",
        "SETCRSPTR", "SETLMEMBASE", "SGXT", "SHF", "SHFL", "SHL", "SHR", "STP", "TLD4S",
        "TLDS", "TMML", "TXA", "TXD", "TXQ", "UBREV", "UFLO", "UIADD3", "UIMAD", "UISETP",
        "ULDC", "ULEA", "ULOP3", "UMOV", "UP2UR", "UPLOP3", "UPOPC", "UPRMT", "USEL",
        "USGXT", "USHF", "VABSDIFF", "VABSDIFF4", "VADD", "VMAD", "VMNMX", "VOTE", "VOTEU",
        "VSET", "VSETP", "VSHL", "VSHR", "XMAD"
    ],
}

