from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, test_locator):
        self.driver.find_element(*test_locator).click()

    @allure.step('Подождать прогрузки элемента')
    def waiting_for_element(self, test_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(test_locator))

    @allure.step('Подождать пока загрузится страница')
    def waiting_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Проверить видимость элемента')
    def if_element_is_displayed(self, test_locator):
        return self.driver.find_element(*test_locator).is_displayed()

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, test_locator):
        element = self.driver.find_element(*test_locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ввести текст в поле')
    def text_input_field(self, test_locator, text):
        self.driver.find_element(*test_locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, test_locator):
        return self.driver.find_element(*test_locator).text

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url
