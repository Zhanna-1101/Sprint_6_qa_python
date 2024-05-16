import allure
from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Подождать до появления кнопки "Заказать"')
    def wait_for_button_order_is_visible(self, button):
        self.waiting_for_element(button)

    @allure.step('Проскроллить до кнопки "Заказать"')
    def scroll_to_button_order(self, button):
        self.scroll_to_element(button)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order(self, button):
        self.click_on_element(button)

    @allure.step('Заполнение всех полей формы "Для кого самокат" и нажатие кнопки "Дальше"')
    def fill_page_personal_info(self, user_data):
        self.waiting_for_element(OrderPageLocators.FIELD_NAME)
        self.click_on_element(OrderPageLocators.FIELD_NAME)
        self.text_input_field(OrderPageLocators.FIELD_NAME, user_data[0])
        self.click_on_element(OrderPageLocators.FIELD_SURNAME)
        self.text_input_field(OrderPageLocators.FIELD_SURNAME, user_data[1])
        self.click_on_element(OrderPageLocators.FIELD_ADDRESS)
        self.text_input_field(OrderPageLocators.FIELD_ADDRESS, user_data[2])
        self.click_on_element(OrderPageLocators.FIELD_SUBWAY)
        self.scroll_to_element(OrderPageLocators.LIST_METRO_STATION(user_data[3]))
        self.click_on_element(OrderPageLocators.LIST_METRO_STATION(user_data[3]))
        self.click_on_element(OrderPageLocators.FIELD_MOBILE_NUMBER)
        self.text_input_field(OrderPageLocators.FIELD_MOBILE_NUMBER, user_data[4])
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение всех полей формы "Про аренду" и подтвеждение заказа')
    def fill_page_rent_info(self, user_data):
        self.waiting_for_element(OrderPageLocators.FIELD_DATE)
        self.click_on_element(OrderPageLocators.FIELD_DATE)
        self.click_on_element(OrderPageLocators.CHOOSE_DATE(user_data[5]))
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.CHOOSE_PERIOD(user_data[6]))
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_SCOOTER(user_data[7]))
        self.click_on_element(OrderPageLocators.FIELD_COMMENT)
        self.text_input_field(OrderPageLocators.FIELD_COMMENT, user_data[8])
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.waiting_for_element(OrderPageLocators.HEADER_CONFIRM_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step('Проверка появления кнопки "Посмотреть статус" в окне Заказ оформлен')
    def check_that_button_check_order_is_displayed(self):
        return self.if_element_is_displayed(OrderPageLocators.BUTTON_CHECK_STATUS)
