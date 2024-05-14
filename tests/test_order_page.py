import pytest
import allure
from pages.order_page import OrderPage
from locators.locators_order_page import OrderPageLocators
from data import UserSet


class TestOrderPage:
    @allure.title('Проверка создания заказа пользователем')
    @allure.description('Проверка всего флоу позитивного сценария с двумя наборами данных из двух точек входа:: кнопка «Заказать» вверху страницы и внизу.')
    @pytest.mark.parametrize("button_order, user_data", [(OrderPageLocators.BUTTON_ORDER_AT_TOP, UserSet.user_data1),
                                                         (OrderPageLocators.BUTTON_ORDER_AT_BOTTOM, UserSet.user_data2)])
    def test_order_flow_from_both_button_order(self, driver, button_order, user_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_button_order(button_order)
        order_page.wait_for_button_order_is_visible(button_order)
        order_page.click_button_order(button_order)
        order_page.fill_page_personal_info(user_data)
        order_page.fill_page_rent_info(user_data)
        assert order_page.check_that_button_check_order_is_displayed()
