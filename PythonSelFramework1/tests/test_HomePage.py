import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from testdata import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, get_data):

        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["lastname"])
        homepage.get_check_box().click()
        self.select_option_by_test(homepage, get_data["gender"])
        homepage.get_submit_form().click()
        success_text = homepage.get_alert().text
        assert "Success" in success_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
