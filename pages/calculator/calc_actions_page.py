from pages.calculator.base_page import BasePage

class CalcActionsPage(BasePage):

    def summarize_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_plus()
        self.click_number(num2)
        self.click_equal()
        return self.get_result()
    
    def subtract_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_minus()
        self.click_number(num2)
        self.click_equal()
        return self.get_result()
    
    def make_square_number(self, num1) -> int:
        self.click_number(num1)
        self.click_square()
        return self.get_result()