from pages.vscode.base_page import BaseVSCodePage

class VSCodeActionsPage(BaseVSCodePage):
    def open_explorer(self):
        self.explorer_button.wait("enabled", timeout=5).click_input()

    def open_search(self):
        self.search_button.wait("enabled", timeout=5).click_input()

    def type_in_editor(self, text: str):
        self.editor.wait("enabled", timeout=5).set_focus()
        self.editor.type_keys(text, with_spaces=True)

    def open_extensions(self):
        self.extensions_button.wait("enabled").click_input()

    def search_extension(self, name: str):
        self.extensions_search.wait("enabled").set_focus()
        self.extensions_search.type_keys(name, with_spaces=True)
        self.necessary_extension.click_input()

    def create_new_file(self):
        self.explorer_button.click_input()
        self.new_file_button.wait("enabled").click_input()
        self.window.type_keys(filename + "{ENTER}")

    def type_code(self, text: str):
        self.editor_area.wait("enabled").set_focus()
        self.editor_area.type_keys(text, with_spaces=True)

    def install_extension(self):
        self.window.child_window(
            name="Install",
            control_type="Button"
        ).wait("enabled", timeout=20).click_input()

    def is_installed(self):
        return self.window.child_window(
            name="Uninstall",
            control_type="Text"
        ).exists()
    
    def save_file(self):
        editor = self.window.child_window(control_type="Document")
        editor.wait("enabled", timeout=5).set_focus()
        editor.type_keys("^s")