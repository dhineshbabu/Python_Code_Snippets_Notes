from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class='card h-100']") #driver.find_elements_by_xpath("//div[@class='card h-100']")
    card_footer = (By.XPATH, "div/h4/a")
    product_button = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def get_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def get_button(self):
        return self.driver.find_element(*CheckoutPage.product_button)