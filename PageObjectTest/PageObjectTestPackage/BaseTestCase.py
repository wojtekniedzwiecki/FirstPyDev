import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        #self.driver = webdriver.Firefox()
        # chromedriver = "D:/Dev/selenium"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # self.driver = webdriver.Chrome(chromedriver)

        self.driver = webdriver.Chrome("D:/Dev/selenium/chromedriver")
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://empik.com/')

    def tearDown(self):
        # close the browser window
        self.driver.quit()