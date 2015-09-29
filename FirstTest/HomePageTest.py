'''
Created on Jun 30, 2015

@author: wojtekniedzwiecki
'''
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page """
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID,"select-language"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = \
            self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        shopping_cart_icon.click()

        shopping_cart_status = \
            self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual("You have no items in your shopping cart.", shopping_cart_status)

        close_button =  self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        close_button.click()


    def test_language_options(self):
        # list of expected values in Language dropdown
        exp_options = ["ENGLISH", "FRENCH", "GERMAN"]

        # empty list for capturing actual options displayed # in the dropdown
        act_options = []

        # get the Your language dropdown as instance of Select class
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))

        # check number of options in dropdown
        self.assertEqual(2, len(select_language.options))

        # get options in a list
        for option in select_language.options:
            act_options.append(option.text)

        # check expected options list with actual options list
        self.assertListEqual(exp_options, act_options)

        # check default selected option is English
        self.assertEqual("ENGLISH", select_language.first_selected_option.text)

        # select an option using select_by_visible text
        select_language.select_by_visible_text("German")

        # check store is now German
        self.assertTrue("store=german" in self.driver.current_url)

        # changing language will refresh the page,
        # we need to get find language dropdown once again
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)


    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()


    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    if __name__ == '__main__':
        unittest.main(verbosity=2)