from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit_form = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_check_box(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit_form(self):
        return self.driver.find_element(*HomePage.submit_form)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)