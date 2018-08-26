import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class U_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_U_Test(self):
        driver = self.driver
        driver.get("https://www.facebook.com")

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    main()