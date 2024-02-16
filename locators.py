from selenium.webdriver.common.by import By

class TestLocators:
    #Авторизация 
    INPUT_EMAIL_AUTHORIZATION = By.NAME, 'name' #Поле вводе email на странице авторизации
    INPUT_PASSWORD_AUTHORIZATION = By.NAME, 'Пароль' #Поле вводе пароль на странице авторизации
    SUBMIT_BUTTON_AUTHORIZATION = By.CLASS_NAME, 'button_button__33qZ0' #Кнопка авторизации

    #Регистрация
    INPUT_EMAIL_REGISTRATION = By.XPATH, "//label[text()='Email']/ancestor::fieldset//input" #Поле вводе email на странице регистрации
    INPUT_PASSWORD_REGISTRATION = By.XPATH, ".//input[@name = 'Пароль']"  #Поле вводе имя на странице регистрации
    INPUT_NAME_REGISTRATION = By.XPATH, ".//input[@name = 'name']" #Поле вводе имя на странице регистрации
    SUBMIT_BUTTON_REGISTRATION = By.CLASS_NAME, 'button_button__33qZ0' #Кнопка регистрации 
 
    #Переходы
    GO_TO_AUTHORIZATION_PAGE_FROM_MAIN = By.CLASS_NAME, "button_button__33qZ0" #Кнопка перехода на страницу авторизации с главной страницы
    GO_TO_AUTHORIZATION_PAGE_FROM_REGISTRATION_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj' #Кнопка перехода на страницу авторизации со страницы регистрации
    GO_TO_AUTHORIZATION_PAGE_FROM_RECOVERY_PASSWORD_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj'#Кнопка перехода на страницу авторизации со страницы сброса пароля
    GO_TO_REGISTRATION_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj' #Кнопка перехода на страницу регистрации
    GO_TO_PERSONAL_ACCOUNT_PAGE = By.LINK_TEXT, 'Личный Кабинет' #Кнопка перехода на страницу личный кабинет
    GO_TO_RECOVERY_PASSWORD_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj' #Кнопка перехода на страницу сброс пароля
    EXIT_FROM_ACCOUNT = By.CLASS_NAME, 'Account_button__14Yp3' #Кнопка Выхож из аккаунта
    GO_TO_CONSTRUCTOR = By.CLASS_NAME, 'AppHeader_header__linkText__3q_va'#Переход на конструктор 
    GO_TO_TAB_BUNS = By.XPATH, ".//span[text() = 'Булки']" #Кнопка Булки для перехода по табам конструктора бургеар
    GO_TO_TAB_TOPPINGS = By.XPATH, ".//span[text() = 'Начинки']"#Кнопка Начинки для перехода по табу конструктора
    GO_TO_TAB_SOUSES = By.XPATH, ".//span[text() = 'Соусы']"#Кнопка Соусы для перехода по табу конструктора
    
    
    #Всякие локаторы для проверки 
    INCORRECT_PASSWORD_TEXT = By.CLASS_NAME, 'input__error' #Текст Некорретный пароль 
    ARE_YOU_NEW_USER = By.LINK_TEXT, 'Вы — новый пользователь?' #Локатор страницы авторизации
    CHECK_OF_BUNS = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Булки']" # Локатор для WebDriverWait Краторная булка карточка булки
    CHECK_OF_TOPPINGS = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Начинки']" #Локатор для WebDriverWait Начинка
    CHECK_OF_OF_SAUCE = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Соусы']"#Локатор для WebDriverWait Соус
    PROFILE_BUTTON = By.CLASS_NAME,'Account_link__2ETsJ'  # Кнопка Профиль в личном кабинете
    SELECTOR_BURGER = By.XPATH, ".//div[@style = 'display: flex;']" #Селектор ингрдиентов
    LOGO_MAIN_PAGE = By.CLASS_NAME, 'AppHeader_header__logo__2D0X2' # Лого в хэдере
    ENTER_TEXT = By.XPATH, ".//h2[text() = 'Вход']" # Надпись вход на странице авторизации
    CARD_OF_SAUCE = By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa72"]' #Карточка с соусом Spicy-X
    CARD_OF_BUN = By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa6d"]'#Карточка с булкой R2-D3
    CARD_OF_TOPPINGS = By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa76"]'#Карточка с начинкой Хрустящие Минеральные Кольца