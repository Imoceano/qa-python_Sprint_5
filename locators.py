from selenium.webdriver.common.by import By

class TestLocators:
    #Авторизация 
    INPUT_EMAIL_AUTHORIZATION = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input' #Поле вводе email на странице авторизации
    INPUT_PASSWORD_AUTHORIZATION = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' #Поле вводе пароль на странице авторизации
    SUBMIT_BUTTON_AUTHORIZATION = By.XPATH, '//*[@id="root"]/div/main/div/form/button' #Кнопка авторизации

    #Регистрация
    INPUT_EMAIL_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' #Поле вводе email на странице регистрации
    INPUT_PASSWORD_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'  #Поле вводе имя на странице регистрации
    INPUT_NAME_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input' #Поле вводе имя на странице регистрации
    SUBMIT_BUTTON_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/button' #Кнопка регистрации 
 
    #Переходы
    GO_TO_AUTHORIZATION_PAGE = By.CLASS_NAME, "button_button__33qZ0" #Кнопка перехода на страницу авторизации с главной страницы
    GO_TO_REGISTRATION_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj' #Кнопка перехода на страницу регистрации
    GO_TO_PERSONAL_ACCOUNT_PAGE = By.XPATH, '//*[@id="root"]/div/header/nav/a/p' #Кнопка перехода на страницу личный кабинет
    GO_TO_RECOVERY_PASSWORD_PAGE = By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a' #Кнопка перехода на страницу сброс пароля
    EXIT_FROM_ACCOUNT = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button' #Кнопка Выхож из аккаунта
    GO_TO_CONSTRUCTOR = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p'#Переход на конструктор 
    GO_TO_TAB_BUNS = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p' #Кнопка Булки для перехода по табам конструктора бургеар
    GO_TO_TAB_TOPPINGS = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p'#Кнопка Начинки для перехода по табу конструктора
    GO_TO_TAB_SOUSES = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]/p'#Кнопка Соусы для перехода по табу конструктора
    
    
    #Всякие локаторы для проверки 
    INCORRECT_PASSWORD_TEXT = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p' #Текст Некорретный пароль 
    ARE_YOU_NEW_USER =  By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]' #Локатор страницы авторизации
    CARD_OF_BUNS = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]' # Локатор для WebDriverWait Краторная булка карточка булки
    CARD_OF_TOPPINGS = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]' #Локатор для WebDriverWait Начинка
    CARD_OF_SAUCE = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]'#Локатор для WebDriverWait Соус