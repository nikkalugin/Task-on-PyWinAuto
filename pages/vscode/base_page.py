from pywinauto import Desktop

class BaseVSCodePage:
    def __init__(self, app):
        self.app = app
        self.window = Desktop(backend="uia").window(title_re=".*Visual Studio Code.*")
        self.window.wait("visible", timeout=5)

    @property
    def explorer_button(self):
        return self.window.child_window(title="Explorer", control_type="Button")

    @property
    def search_button(self):
        return self.window.child_window(title="Search", control_type="Button")

    @property
    def editor(self):
        return self.window.child_window(auto_id="workbench.parts.editor")