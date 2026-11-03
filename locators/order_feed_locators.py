from selenium.webdriver.common.by import By

FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

TOTAL_COMPLETED_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
TODAY_COMPLETED_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

# в вёрстке класс orderListReady стоит на колонке «В работе», названия перепутаны
ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'orderListReady')]/li")
