from pages.standard_page import StandardPage

def test_summarizing_numbers(app):
    standardPage = StandardPage(app)
    result = standardPage.summarize_numbers(39, 15)
    assert result == 54

def test_subtracting_numbers(app):
    standardPage = StandardPage(app)
    result = standardPage.subtract_numbers(897, 21)
    assert result == 876

def test_squaring_numbers(app):
    standardPage = StandardPage(app)
    result = standardPage.make_square_number(10)
    assert result == 100