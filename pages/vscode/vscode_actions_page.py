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

    def create_new_file(self):
        self.explorer_button.click_input()
        self.new_file_button.wait("enabled").click_input()

    def type_code(self, text: str):
        self.editor_area.wait("enabled").set_focus()
        self.editor_area.type_keys(text, with_spaces=True)