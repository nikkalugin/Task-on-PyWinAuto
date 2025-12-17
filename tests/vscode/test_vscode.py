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

def test_open_extensions_and_search(vscode_app):
    page = VSCodeActionsPage(vscode_app)
    page.open_extensions()
    page.search_extension("Python")
    assert page.extensions_search.exists()

def test_create_new_file_and_type_text(vscode_app):
    page = VSCodeActionsPage(vscode_app)
    page.create_new_file()
    page.type_code("Hello, World!")
    assert page.editor_area.exists()