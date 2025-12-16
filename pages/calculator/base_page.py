from pywinauto import Application, Desktop

class BasePage: 

    PLUS_BUTTON = "plusButton"
    MINUS_BUTTON = "minusButton"
    SQUARE_BUTTON = "xpower2Button"
    EQUAL_BUTTON = "equalButton"
    RESULT = "CalculatorResults"

    def __init__(self, app: Application):
        self.app = app
        self.window_app = Desktop(backend="uia").window(
            title_re=".*Calculator.*",
            control_type="Window"
        )
        self.window_app.wait("visible", timeout=4)

    def click_number(self, number: int):
        for digit in str(number):
            self.window_app.child_window(
                auto_id=f"num{digit}Button"
            ).wait("enabled").set_focus().click()

    def click_plus(self):
        self.window_app.child_window(auto_id=self.PLUS_BUTTON).click_input()

    def click_minus(self):
        self.window_app.child_window(auto_id=self.MINUS_BUTTON).click_input()

    def click_equal(self):
        self.window_app.child_window(auto_id=self.EQUAL_BUTTON).click_input()

    def click_square(self):
        self.window_app.child_window(auto_id=self.SQUARE_BUTTON).click_input()

    def get_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.RESULT).texts()
        return int(result[0].split(" ")[2])
    
    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.RESULT).type_keys(number)