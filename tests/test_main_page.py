import pytest
import allure
from pages.main_page import MainPage
from data import QuestionAnswerSet


class TestMainPage:

    @allure.title('Проверка осуществления перехода на главную страницу Дзен по клику на логотип Яндекса')
    def test_logo_yandex_direct_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_yandex_logo_is_visible()
        main_page.click_yandex_logo()
        main_page.go_to_next_tab()
        main_page.wait_for_dzen_url()
        assert main_page.check_current_page_is_dzen()

    @allure.title('Проверка осуществления перехода на главную страницу Самоката по клику на логотип Самоката из страницы заказа')
    def test_logo_scooter_direct_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_button_order_at_top_is_visible()
        main_page.click_button_order_at_the_top()
        main_page.waiting_for_page_order_open()
        main_page.click_scooter_logo()
        assert main_page.check_current_page_is_main()

    @allure.title('Проверка раздела "Вопросы о важном" на главной странице сайта')
    @allure.description('Проверяем, что при нажатии на каждый из вопросов раздела, появляется соответствующий ему ответ')
    @pytest.mark.parametrize("number, expected_result", QuestionAnswerSet.question_answer_set)
    def test_faq_on_main_page(self, driver, number, expected_result):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.scroll_to_faq()
        main_page.wait_for_question_is_visible(number)
        main_page.click_question(number)
        main_page.wait_for_answer_is_visible(number)
        actual_result = main_page.get_answer_text(number)
        assert actual_result == expected_result, 'Ответ не соответствут ожидаемому ответу на вопрос'
