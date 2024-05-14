from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопка "Заказать" в хедере сайта
    BUTTON_ORDER_AT_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")

    # Кнопка "Заказать" под информацией "О том как это работает"
    BUTTON_ORDER_AT_BOTTOM = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"

    # Раздел "Для кого самокат"
    # Заголовок раздела "Для кого самокат"
    HEADER_PAGE_PERSONAL_INFO = By.XPATH, ".//div[text()='Для кого самокат']"

    # Поле "Имя"
    FIELD_NAME = By.XPATH, ".//input[@placeholder='* Имя']"

    # Поле "Фамилия"
    FIELD_SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"

    # Поле "Адрес: куда привезти самокат"
    FIELD_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"

    # Поле "Станция метро"
    FIELD_SUBWAY = By.XPATH, ".//input[@placeholder='* Станция метро']"

    # Метод, который возвращает станцию метро
    @staticmethod
    def LIST_METRO_STATION(data=''):
        return [By.XPATH, f'//li[@data-value="{data}"]']

    # Поле "Телефон: на него позвонит курьер"
    FIELD_MOBILE_NUMBER = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"

    # Кнопка "Далее" на странице заказа
    BUTTON_NEXT = By.XPATH, ".//button[text()='Далее']"

    # Раздел "Про аренду"
    # Заголовок раздела "Про аренду"
    HEADER_PAGE_RENT_INFO = By.XPATH, ".//div[text()='Про аренду']"

    # Поле "Когда привезти самокат"
    FIELD_DATE = By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']"

    # Метод который возвращает дату
    @staticmethod
    def CHOOSE_DATE(data=0):
        return By.CSS_SELECTOR, f".react-datepicker__day--{data}"

    # Поле "Срок аренды" (для клика)
    FIELD_RENTAL_PERIOD = By.XPATH, ".//div[text()='* Срок аренды']"

    # Выбрать количество суток в открытом списке
    @staticmethod
    def CHOOSE_PERIOD(data=''):
        return By.XPATH, f".//div[@class='Dropdown-option' and text()='{data}']"

    # Выбор цвета самоката
    @staticmethod
    def CHECKBOX_COLOR_SCOOTER(data=''):
        return By.XPATH, f".//input[@id='{data}']"

    # Поле "Комментарий для курьера"
    FIELD_COMMENT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"

    # Кнопка "Назад" на странице заказа
    BUTTON_BACK = By.XPATH, ".//button[text()='Назад']"

    # Кнопка "Заказать" на странице заказа
    BUTTON_ORDER = By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"

    # Заголовок окна подтверждения заказа
    HEADER_CONFIRM_ORDER = By.XPATH, ".//div[text()='Хотите оформить заказ?']"

    # Кнопка "Да" окна "Хотите оформить заказ?"
    BUTTON_CONFIRM_ORDER = By.XPATH, ".//button[text()='Да']"

    # Кнопка "Посмотреть статус" в окне "Заказ оформлен"
    BUTTON_CHECK_STATUS = By.XPATH, ".//button[text()='Посмотреть статус']"
