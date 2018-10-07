import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome(os.environ['CHROME_DRIVER'])
        self.browser = webdriver.Chrome('/Users/juniorportom/projects/pruebas/chromedriver')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Reinaldo')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Portocarrero')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3112131313')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('rj.portocarrero281@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/juniorportom/Downloads/logo-1.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('porto')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('prueba123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        # span=self.browser.find_element(By.XPATH, '//span[text()="Reinaldo Portocarrero"]')
        # self.assertIn('Reinaldo Portocarrero', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Reinaldo Portocarrero"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Reinaldo Portocarrero"]')

        self.assertIn('Reinaldo Portocarrero', h2.text)
