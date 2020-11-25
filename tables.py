"""
    Este scrip obtiene el header de una tabla y su contenido
"""

import unittest
from selenium import webdriver

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.implicitly_wait(1)
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver
        table_data = list()

        # Obtengo una lista de los tr en el body de la tabla
        # a dicha lista le aplico un len() y obtenermos cuantos datos hay en el body
        data_size = driver.find_elements_by_xpath('//*[@id="table1"]/tbody/tr')

        # Obtener una lista de los th contenido en el thead de la tabla
        # Con la lista de los th, le aplico un len a la lista y veos cuantos header hay
        header_size = driver.find_elements_by_xpath('//*[@id="table1"]/thead/tr/th')
        

        for i in range(1,len(data_size)+1):
            for j in range(1,len(header_size)): # Omitimos el header action
                header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j}]/span').text
                content = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i}]/td[{j}]').text
                table_data.append({header:content})
        
        print(table_data)
                

            

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
