import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.environ['CHROME_DRIVER'])
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()
