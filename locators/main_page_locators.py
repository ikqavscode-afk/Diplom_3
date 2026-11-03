from selenium.webdriver.common.by import By

_FIRST_CARD = "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]"
_OPENED_MODAL = "//section[contains(@class,'Modal_modal_opened')]"

# первая карточка в списке всегда булка (вкладка «Булки» открыта по умолчанию)
BUN_CARD = (By.XPATH, _FIRST_CARD)
BUN_COUNTER = (By.XPATH, _FIRST_CARD + "//p[contains(@class,'counter_counter__num')]")

CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

# все окна лежат в DOM сразу, открытое отличается классом Modal_modal_opened
OPENED_MODAL = (By.XPATH, _OPENED_MODAL)
INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
MODAL_CLOSE_BUTTON = (By.XPATH, _OPENED_MODAL + "//button[contains(@class,'Modal_modal__close')]")

# до готовности заказа в окне стоит заглушка «9999»
ORDER_NUMBER = (By.CSS_SELECTOR, "h2[class*='Modal_modal__title_shadow']")
MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")