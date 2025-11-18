import sys

LANG_CONFIG = {
    "Python": {
        "ext": ".py",
        "sample": "examples/hello.py",
        "comment": "# ",
        "runner": lambda f: [sys.executable, str(f)]
    },
    "Java": {
        "ext": ".java",
        "sample": "examples/Hello.java",
        "comment": "// ",
        "runner": "java"
    },
    "C": {
        "ext": ".c",
        "sample": "examples/hello.c",
        "comment": "// ",
        "runner": "c"
    },
    "C++": {
        "ext": ".cpp",
        "sample": "examples/hello.cpp",
        "comment": "// ",
        "runner": "cpp"
    },
    "JavaScript": {
        "ext": ".js",
        "sample": "examples/hello.js",
        "comment": "// ",
        "runner": lambda f: ["node", str(f)]
    },
    "TypeScript": {
        "ext": ".ts",
        "sample": "examples/hello.ts",
        "comment": "// ",
        "runner": "typescript"
    },
    "Rust": {
        "ext": ".rs",
        "sample": "examples/hello.rs",
        "comment": "// ",
        "runner": "rust"
    },
    "Go": {
        "ext": ".go",
        "sample": "examples/hello.go",
        "comment": "// ",
        "runner": lambda f: ["go", "run", str(f)]
    },
    "C#": {
        "ext": ".cs",
        "sample": "examples/hello.cs",
        "comment": "// ",
        "runner": "csharp"
    },
    "Ruby": {
        "ext": ".rb",
        "sample": "examples/hello.rb",
        "comment": "# ",
        "runner": lambda f: ["ruby", str(f)]
    },
    "Kotlin": {
        "ext": ".kt",
        "sample": "examples/hello.kt",
        "comment": "// ",
        "runner": "kotlin"
    },
    "HTML": {
        "ext": ".html",
        "sample": "examples/index.html",
        "comment": "<!-- ",
        "runner": "browser"
    },
    "CSS": {
        "ext": ".css",
        "sample": "examples/styles.css",
        "comment": "/* ",
        "runner": "browser"
    },
    "Lua": {
        "ext": ".lua",
        "sample": "examples/hello.lua",
        "comment": "-- ",
        "runner": lambda f: ["lua", str(f)]
    },
    "Nix": {
        "ext": ".nix",
        "sample": "examples/shell.nix",
        "comment": "# ",
        "runner": "nix"
    },
    "PTX": {
        "ext": ".ptx",
        "sample": "examples/hello.ptx",
        "comment": "// ",
        "runner": "ptx"
    }
}
