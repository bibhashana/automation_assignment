
from seleniumpagefactory.Pagefactory import PageFactory
class fieldsearch(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'time':('Xpath','//li[@class="oxd-main-menu-item-wrapper"][4]'),
        'employee':('XPATH','//input[@placeholder="Type for hints..."]'),
        'view':('XPATH','//button[@type="submit"]')
    }

    def click_leave(self):
        self.time.click()

    def employeee(self):
       self.employee.set_text("Paul Collings")

    def click_view(self):
        self.view.click()

