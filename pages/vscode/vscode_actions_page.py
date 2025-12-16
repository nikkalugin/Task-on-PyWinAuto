from pages.vscode.base_page import BaseVSCodePage

class VSCodeActionsPage(BaseVSCodePage):
    def open_explorer(self):
        self.explorer_button.wait("enabled", timeout=5).click_input()

    def open_search(self):
        self.search_button.wait("enabled", timeout=5).click_input()

    def type_in_editor(self, text: str):
        self.editor.wait("enabled", timeout=5).set_focus()
        self.editor.type_keys(text, with_spaces=True)