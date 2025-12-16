import pytest
from pywinauto import Application, Desktop

@pytest.fixture
def app():
    app = Application(backend="uia").start("calc.exe")
    yield app

    try:
        window = Desktop(backend="uia").window(title_re=".*Calculator.*")
        window.close()
    except Exception:
        pass
    # app.kill()