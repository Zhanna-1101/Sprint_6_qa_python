import allure
from pages.base_page import BasePage
from locators.locators_main_page import MainPageLocators
from locators.locators_order_page import OrderPageLocators
from data import Urls


class MainPage(BasePage):

    @allure.step('Подождать появления логотипа Яндекса')
    def wait_for_yandex_logo_is_visible(self):
        self.waiting_for_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Кликнуть на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Подождать загрузки страницы Дзен')
    def wait_for_dzen_url(self):
        self.waiting_for_url(Urls.DZEN_PAGE_URL)

    @allure.step('Подождать до появления кнопки "Заказать" в хедере')
    def wait_for_button_order_at_top_is_visible(self):
        self.waiting_for_element(OrderPageLocators.BUTTON_ORDER_AT_TOP)

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_button_order_at_the_top(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER_AT_TOP)

    @allure.step('Подождать пока загрузится страница оформления заказа')
    def waiting_for_page_order_open(self):
        return self.waiting_for_url(Urls.ORDER_PAGE_URL)

    @allure.step('Подождать появления логотипа Самоката')
    def wait_for_scooter_logo_is_visible(self):
        self.waiting_for_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Поверить что текущая страница является главной страницей сайта')
    def check_current_page_is_main(self):
        return self.current_url() == Urls.MAIN_PAGE_URL

    @allure.step('Проверить что текущая страница является страницей сайта Дзен')
    def check_current_page_is_dzen(self):
        return self.current_url() == Urls.DZEN_PAGE_URL

    @allure.step('Принять куки')
    def accept_cookie(self):
        self.click_on_element(MainPageLocators.BUTTON_COOKIE)

    @allure.step('Проскроллить до блока с вопросами о важном')
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.BLOCK_FAQ)

    @allure.step('Подождать до появления вопроса с соответствующим номером')
    def wait_for_question_is_visible(self, number):
        self.waiting_for_element(MainPageLocators.questions[number])

    @allure.step('Кликнуть на вопрос в блоке с вопросами')
    def click_question(self, number):
        self.click_on_element(MainPageLocators.questions[number])

    @allure.step('Подождать до появления ответа на вопрос')
    def wait_for_answer_is_visible(self, number):
        self.waiting_for_element(MainPageLocators.answers[number])

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text(self, number):
        return self.get_text_of_element(MainPageLocators.answers[number])
