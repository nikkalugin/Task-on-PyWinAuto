import pytest
import os
from pywinauto import Application, Desktop

# ---- Calculator ----

@pytest.fixture(scope="session")
def calculator_app():
    app = Application(backend="uia").start("calc.exe")
    yield app

    try:
        window = Desktop(backend="uia").window(title_re=".*Calculator.*")
        window.close()
    except Exception:
        pass

# ---- VSCode ----

@pytest.fixture(scope="session")
def vscode_app():
    vscode_path = r"C:\Users\QA-user\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    app = Application(backend="uia").start(vscode_path)
    yield app
    
    try:
        window = Desktop(backend="uia").window(title_re=".*Virtual Studio Code.*")
        window.close()
    except Exception:
        pass