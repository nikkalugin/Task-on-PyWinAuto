from pages.vscode.vscode_actions_page import VSCodeActionsPage

def test_open_search(vscode_app):
    page = VSCodeActionsPage(vscode_app)
    page.open_search()
    assert page.search_button.is_enabled()

def test_type_in_editor(vscode_app):
    page = VSCodeActionsPage(vscode_app)
    page.type_in_editor("Hello VSCode!")
    editor_text = page.editor.window_text()
    assert "Hello VSCode!" in editor_text