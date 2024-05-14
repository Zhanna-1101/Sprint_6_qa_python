from selenium.webdriver.common.by import By


class MainPageLocators:

    # Логотип Яндекс
    LOGO_YANDEX = By.XPATH, ".//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]"

    # Логотип Самокат
    LOGO_SCOOTER = By.XPATH, ".//a[@href='/' and contains(@class, 'Header_LogoScooter')]"

    # Заголовок на главной странице
    HEADER_OF_MAIN_PAGE = By.XPATH, ".//div[contains(@class, 'Home_Header')]/[text()='Самокат']"

    # Кнопка согласия с куками
    BUTTON_COOKIE = (By.ID, 'rcc-confirm-button')

    # Кнопка "Статус заказа"
    BUTTON_STATUS_ORDER = By.XPATH, ".//button[text()='Статус заказа']"

    # Вопросы о важном
    # Блок с вопросами о важном
    BLOCK_FAQ = (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]")

    # Вопросы
    questions = [(By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-0']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-1']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-2']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-3']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-4']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-5']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-6']"),
                 (By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-7']")]

    # Ответы
    answers = [(By.XPATH, ".//div[@id='accordion__panel-0']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-1']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-2']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-3']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-4']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-5']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-6']/p"),
               (By.XPATH, ".//div[@id='accordion__panel-7']/p")]
