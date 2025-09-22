import logging

import pytest
from selenium import webdriver
from Framework_nopcommerce.PageObjectModel.Loginpage import Login
from Framework.utilities.readproperties import read_config
from Framework.utilities.Customlogger import Loggen


class Test_001_Login:
    baseurl = read_config.get_app_url()  #read property file function used to fetch url ,username and password
    username = read_config.get_username()
    password = read_config.get_password()
    log=Loggen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_title_match(self,setup): #setup is a fixture which is getting called from conftest.py file to start our driver
        self.driver=setup #chrome driver initialization
        self.driver.get(self.baseurl)
        act_ttl=self.driver.title
        self.log.info("******** Test_001_Login ***********")

        if act_ttl=="nopCommerce demo store. Login":
            assert True
            self.log.info("******** Login page title verification test case passed ***********")
        else:
            self.driver.save_screenshot(".\\Framework\\Screenshots\\" +"test_title_match.png")
            self.driver.close()
            self.log.error("******** Login page title verification test case Failed ***********")
            assert False


    def test_login_page(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lgp=Login(self.driver) #lgp object is created to access the page object username password action methods
        self.lgp.setUsername(self.username)
        self.lgp.setpassword(self.password)
        self.lgp.click_login()
        act_ttl=self.driver.title
        if act_ttl=="Dashboard / nopCommerce administration":
            assert True
            self.log.info("************ Dashboard title match passed **********")
        else:
            self.driver.save_screenshot(".\\Framework\\Screenshots\\test_login_page.png")
            self.driver.close()
            self.log.error("************ Dashboard title match Failed **********")
            assert False









