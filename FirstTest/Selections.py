__author__ = 'wojtekniedzwiecki'

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


    def test_language_options(self):
        # list of expected values in Language dropdown
        exp_options = ["ENGLISH", "FRENCH", "GERMAN"]

        # empty list for capturing actual options displayed # in the dropdown
        act_options = []

        # get the Your language dropdown as instance of Select class
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))

        # check number of options in dropdown
        self.assertEqual(3, len(select_language.options))

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
        self.assertTrue("store=german&___from_store" in self.driver.current_url)

        # changing language will refresh the page,
        # we need to get find language dropdown once again
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)


    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
