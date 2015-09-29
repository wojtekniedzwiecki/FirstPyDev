'''
Created on Jul 28, 2015

@author: wojtekniedzwiecki
'''
import unittest
import HTMLTestRunner
import os
from FirstTest import SearchTest
from FirstTest import HomePageTest

# get the directory path to output report file
dir = os.getcwd()
print(dir)

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest.SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest.HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")


# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=outfile,
                 title='Test Report',
                 description='Smoke Tests'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)