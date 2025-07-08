import logging

import pytest
from selenium import webdriver
from Framework.PageObjectModel.Loginpage import Login
from Framework.utilities.readproperties import read_config
from Framework.utilities.Customlogger import Loggen
from Framework.utilities import Excelutil


class Test_002_Login:
    baseurl = read_config.get_app_url()
    username = read_config.get_username()
    password = read_config.get_password()
    path = ".//Testdata//datadriven.xlsx"
    log=Loggen.loggen()



    def test_login_page(self,setup):
        self.log.info("----------Test 002 started---------")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lgp=Login(self.driver) #lgp object is created to access the page object username password action methods
        self.rowcount=Excelutil.rowcount(self.path,'Sheet1')
        print("Row count is : ",self.rowcount)

        lst_status = []

        for r in range (2,self.rowcount+1):
            self.uname=Excelutil.readdata(self.path,'Sheet1',r,1)
            self.pwd=Excelutil.readdata(self.path,'Sheet1',r,2)
            self.exp=Excelutil.readdata(self.path,'Sheet1',r,3)

            self.lgp.setUsername(self.uname)
            self.lgp.setUsername(self.pwd)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    lst_status.append("Pass")
                    self.log.info("--Passed----")
                    self.lgp.click_logout()

                elif self.exp=='Fail':
                    lst_status.append("Fail")
                    self.log.info("---Failed----")
                    self.lgp.click_logout()

            elif act_title!=exp_title:
                if self.exp=='Fail':
                    lst_status.append("Pass")
                    self.log.info("--Passed----")

                elif self.exp=="Pass":
                    lst_status.append("Fail")

            if "Fail" not in lst_status:
                self.driver.close()
                self.log.info("-------Test is considered as passed-------")
            else :
                self.log.info("--------Consider test as Failed-----------")
                self.driver.close()










