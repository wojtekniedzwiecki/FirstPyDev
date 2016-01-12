from base import BasePage
from base import InvalidPageException
from product import ProductPage

class SearchRegion(BasePage):
    _search_box_locator = 'q-i'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)

class SearchResults(BasePage):
    _product_list_locator   = 'div.contentSearchPacket div.productsSet > div'
    #_product_list_locator = "//div[@class='productsSet']/div"
    _product_name_locator   = 'div.productsSet div.productBox-450Desc > a'
    _product_image_link     = 'div.productsSet div.productBox-450Pic'
    #_page_title_locator     = 'div.page-title'

    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements_by_css_selector(self._product_list_locator)
        #results = self.driver.find_elements_by_xpath(self._product_list_locator)

        for product in results:
            name = product.find_element_by_css_selector(self._product_name_locator).text
            self._products[name] = product.find_element_by_css_selector(self._product_image_link)

    def _validate_page(self, driver):
        if 'sklep internetowy' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
         self._products[product_name].click()
         return ProductPage(self.driver)