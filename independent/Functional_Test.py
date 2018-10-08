import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.environ['CHROME_DRIVER'])
        # self.browser = webdriver.Chrome('/Users/juniorportom/projects/pruebas/chromedriver')
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
        span=self.browser.find_element(By.XPATH, '//span[text()="Reinaldo Portocarrero"]')
        self.assertIn('Reinaldo Portocarrero', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Pepe')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Perez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3112131313')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('pp.p@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/juniorportom/Downloads/logo-1.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('porto')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('prueba123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Pepe Perez"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Pepe Perez"]')

        self.assertIn('Pepe Perez', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_usrname')
        nombreUsuario.send_keys('porto')

        clave = self.browser.find_element_by_id('id_psw')
        clave.send_keys('prueba123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()

        self.browser.implicitly_wait(3)

        h3=self.browser.find_element(By.XPATH, '//h3[text()="Administrar"]')
        self.assertIn('Administrar', h3.text)

    def test_editar_perfil(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_usrname')
        nombreUsuario.send_keys('porto')

        clave = self.browser.find_element_by_id('id_psw')
        clave.send_keys('prueba123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()

        self.browser.implicitly_wait(3)

        h3 = self.browser.find_element(By.XPATH, '//h3[text()="Administrar"]')
        self.assertIn('Administrar', h3.text)

        link = self.browser.find_element_by_id('id_editar')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Sebastian')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Martinez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('1')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('300000000')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        logout = self.browser.find_element_by_id('id_logout')
        logout.click()
        self.browser.implicitly_wait(3)

        span=self.browser.find_element(By.XPATH, '//span[text()="Sebastian Martinez"]')
        self.assertIn('Sebastian Martinez', span.text)

    def test_registro_comentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Pepe Perez"]')
        span.click()

        correo = self.browser.find_element_by_id('correo')
        correo.clear()
        correo.send_keys('s.fernandes@gmail.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.clear()
        comentario.send_keys('Este es un comentario')

        botonGrabar = self.browser.find_element_by_id('id_addComent')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        h4=self.browser.find_element(By.XPATH, '//h4[text()="s.fernandes@gmail.com"]')
        self.assertIn('s.fernandes@gmail.com', h4.text)
