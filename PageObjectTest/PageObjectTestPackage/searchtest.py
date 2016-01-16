import unittest
from homepage import HomePage
from basetestcase import BaseTestCase

class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('earphones')
        self.assertEqual(2, search_results.product_count)
        product = search_results.open_product_page('Don\'t Be Fake')
        product.add_to_basket()
        self.assertEqual('Don\'t Be Fake', product.name)
        self.assertEqual('29,99', product.price)
        self.assertEqual('(0)', product.stock_status)


if __name__ == '__main__':
    unittest.main(verbosity=2)