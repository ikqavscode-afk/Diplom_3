from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")
ORDER_FEED_LINK = (By.CSS_SELECTOR, "header a[href='/feed']")
PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")
