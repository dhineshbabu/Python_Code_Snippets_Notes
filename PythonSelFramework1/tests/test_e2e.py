import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.usefixtures("setup") - using this fixture from parent class
from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        home_page.shop_items().click()
        log.info("Getting all the card titles")
        # checkout_page = CheckoutPage(self.driver)
        # products = checkout_page.get_card_titles()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == "Blackberry":
                # add item to the cart
                product.find_element_by_xpath("div/button").click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verify_link_presence("India")
        self.driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success_text = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is ", success_text)
        assert "Success! Thank you!" in success_text