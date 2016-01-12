from base import BasePage
from base import InvalidPageException

class HomePage(BasePage):

    home_page_layout_locator = 'div#layout'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self.home_page_layout_locator)
            # driver.find_elements_by_xpath("//div[@id='layout']")
        except:
            raise InvalidPageException("Home Page not loaded")