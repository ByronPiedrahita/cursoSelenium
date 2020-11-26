import unittest
from selenium import webdriver
from api_data_mock import ApiDataMock
from selenium.webdriver.support.ui import Select # Modulo para poder seleccionar del dropdown
from time import sleep
from selenium.webdriver.common.by import By #Hacer referencia a un elemento del sitio web, para interactuar
from selenium.webdriver.support.ui import WebDriverWait # Modulo para  manejo de esperas explicitas
from selenium.webdriver.support import expected_conditions as EC #esperas explicitas

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.mercadolibre.com') # adiconar la pagina

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()
        sleep(2)

        search_field = driver.find_element_by_name('as_word')
        #country.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(2)

        location = driver.find_element_by_xpath('/html/body/main/div/div/aside/section[2]/dl[8]/dd[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", location)
        # location.click()
        sleep(2)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        #order_menu.click()
        higher_price = driver.find_element_by_class_name('andes-list__item-text')
        #higher_price.click()
        sleep(2)

        #data_size = driver.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol/li')
        
        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i + 1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2').text
            article_price = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i + 1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-result__content-columns > div.ui-search-result__content-column.ui-search-result__content-column--left > div.ui-search-item__group.ui-search-item__group--price > div > div > span.price-tag.ui-search-price__part > span.price-tag-fraction').text
            articles.append(article_name)
            prices.append(article_price)

        print(articles, prices)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)