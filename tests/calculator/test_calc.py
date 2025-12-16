from pages.calculator.calc_actions_page import CalcActionsPage

def test_summarizing_numbers(calculator_app):
    standardPage = CalcActionsPage(calculator_app)
    result = standardPage.summarize_numbers(39, 15)
    assert result == 54

def test_subtracting_numbers(calculator_app):
    standardPage = CalcActionsPage(calculator_app)
    result = standardPage.subtract_numbers(897, 21)
    assert result == 876

def test_squaring_numbers(calculator_app):
    standardPage = CalcActionsPage(calculator_app)
    result = standardPage.make_square_number(10)
    assert result == 100