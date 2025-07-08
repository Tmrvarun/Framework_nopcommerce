import pytest
from selenium import webdriver
from Framework.PageObjectModel.Loginpage import Login
from Framework.PageObjectModel.Add_customer_pom import Add_customer
from Framework.utilities.readproperties import read_config
from Framework.PageObjectModel.Search_customer import Customer_search


class Search_Customer_001():
    baseurl = read_config.get_app_url()
    username = read_config.get_username()
    password = read_config.get_password()

    @pytest.mark.regression
    def search_email_1(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.Login=Login(self.driver)
        self.Login.setUsername(self.username)
        self.Login.setpassword(self.password)
        self.Login.click_login()

        self.lp2 = Add_customer(self.driver)
        self.lp2.click_on_customer_menu()
        self.lp2.set_customer_role()


        self.searchByemail = Customer_search(self.driver)
        self.searchByemail.box_email_id("steve_gates@nopCommerce.com")
        self.searchByemail.search_button()
        self.status = self.searchByemail.row_email_search("steve_gates@nopCommerce.com")
        assert True == self.status
