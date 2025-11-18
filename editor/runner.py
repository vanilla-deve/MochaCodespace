import subprocess
import webbrowser
from pathlib import Path
from qt_compat import QThread, Signal

from config.languages import LANG_CONFIG

class RunnerThread(QThread):
    """Thread for running code without blocking UI"""
    output = Signal(str)
    finished = Signal()

    def __init__(self, command, cwd):
        super().__init__()
        self.command = command
        self.cwd = cwd

    def run(self):
        try:
            process = subprocess.Popen(
                self.command,
                cwd=self.cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate(timeout=60)

            if stdout:
                self.output.emit(stdout)
            if stderr:
                self.output.emit(stderr)

        except subprocess.TimeoutExpired:
            self.output.emit("\n[Execution timeout after 60 seconds]\n")
        except Exception as e:
            self.output.emit(f"\n[Error: {str(e)}]\n")
        finally:
            self.finished.emit()


def get_run_command(filepath: Path, language: str, runner):
    """
    Return a list command to run the file or None if not available.
    This mirrors the logic from original single-file implementation,
    but simplified and centralized here.
    """
    if callable(runner):
        return runner(filepath)

    if runner == "browser":
        webbrowser.open(str(filepath.resolve().as_uri()))
        return None

    # Java
    if runner == "java":
        try:
            subprocess.run(["javac", str(filepath)], check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Java compiler (javac) not found in PATH")
        return ["java", filepath.stem]

    # C
    if runner == "c":
        exe = filepath.with_suffix(".out")
        try:
            subprocess.run(["gcc", str(filepath), "-o", str(exe)], check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("C compiler (gcc) not found in PATH")
        return [str(exe)]

    # C++
    if runner == "cpp":
        exe = filepath.with_suffix(".out")
        try:
            subprocess.run(["g++", str(filepath), "-o", str(exe)], check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("C++ compiler (g++) not found in PATH")
        return [str(exe)]

    # Rust
    if runner == "rust":
        exe = filepath.with_suffix(".out")
        try:
            subprocess.run(["rustc", str(filepath), "-o", str(exe)], check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Rust compiler (rustc) not found in PATH")
        return [str(exe)]

    # TypeScript
    if runner == "typescript":
        js_file = filepath.with_suffix(".js")
        try:
            subprocess.run(["tsc", str(filepath)], check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("TypeScript compiler (tsc) not found in PATH")
        # run with node
        try:
            subprocess.run(["node", "--version"], check=True, capture_output=True)
            return ["node", str(js_file)]
        except (subprocess.CalledProcessError, FileNotFoundError):
            webbrowser.open(str(js_file.resolve().as_uri()))
            return None

    # Kotlin
    if runner == "kotlin":
        jar_file = filepath.parent / "output.jar"
        try:
            subprocess.run(["kotlinc", str(filepath), "-include-runtime", "-d", str(jar_file)],
                           check=True, cwd=str(filepath.parent), capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compilation failed:\n{e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Kotlin compiler (kotlinc) not found in PATH")
        return ["java", "-jar", str(jar_file)]

    # C#
    if runner == "csharp":
        try:
            subprocess.run(["dotnet", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError(".NET SDK not found in PATH")
        return ["dotnet", "run"]

    # Nix
    if runner == "nix":
        try:
            subprocess.run(["nix", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("Nix not found in PATH")
        if filepath.name == "flake.nix":
            return ["nix", "develop", "."]
        else:
            return ["nix-shell", str(filepath)]

    # Fallback: interpreter names in LANG_CONFIG could be lambdas handled above
    return None
