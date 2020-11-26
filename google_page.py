import unittest
from selenium import webdriver
from google_page import GooglePage

class GooglePage(unittest.TestCase):
    print("ENTRO")
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)