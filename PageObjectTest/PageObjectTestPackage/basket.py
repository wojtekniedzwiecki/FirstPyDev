from base import BasePage


class Basket(BasePage):
    _basket_image = 'span.imageBasket'

    def __init__(self, driver):
        super(Basket, self).__init__(driver)

    def openBasket(self):
        self.driver.find_element_by_css_selector(self._basket_image).click()