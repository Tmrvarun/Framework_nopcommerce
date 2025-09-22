import logging

import pytest
from selenium import webdriver
from Framework.PageObjectModel.Loginpage import Login
from Framework.utilities.readproperties import read_config
from Framework.utilities.Customlogger import Loggen
from Framework.utilities import Excelutil


class Test_002_Login:
    baseurl = read_config.get_app_url()
    # username = read_config.get_username()
    # password = read_config.get_password()
    path = ".//Testdata//datadriven.xlsx" #excel sheet path
    log=Loggen.loggen()

#Logic is to verify the title of pages with the sheet username/password as sometimes the login is successful but page tile differs

#The if/else block verifies the expected pass/fail result with Excel sheet and store it in a blank list , if all blank list has pass stored then our test passes else test fails
#we take username/password from loop instead of using it from properties file

    def test_login_page(self,setup):
        self.log.info("----------Test 002 started---------")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lgp=Login(self.driver) #lgp object is created to access the page object username password action methods
        self.rowcount=Excelutil.rowcount(self.path,'Sheet1') #this statement is calling excel utility file from utilities folder , to call we need to pass
                                                                #one is path of sheet and other is sheet name
        print("Row count is : ",self.rowcount) # we take number of rows here

        lst_status = [] #blank list
        for r in range (2,self.rowcount+1): #pass rows here to start the loop and started it from 2 as first row in file is header
            self.uname=Excelutil.readdata(self.path,'Sheet1',r,1) #this will read the username from column 1vof Excel sheet,column 1 of Excel
            self.pwd=Excelutil.readdata(self.path,'Sheet1',r,2) #this will read the password from column 1vof Excel sheet , column 2 of Excel
            self.exp=Excelutil.readdata(self.path,'Sheet1',r,3) #expected result reading , which is in column 3 of sheet

            self.lgp.setUsername(self.uname)
            self.lgp.setUsername(self.pwd)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title: #this statement will verify the title of pages, if successful login , then the titles should match
                if self.exp=='Pass':
                    lst_status.append("Pass")#list to store pass fail
                    self.log.info("--Passed----")
                    self.lgp.click_logout()

                elif self.exp=='Fail': # this condition will check if expected is fail but title is similar
                    lst_status.append("Fail")
                    self.log.info("---Failed----")
                    self.lgp.click_logout()

            elif act_title!=exp_title: #this condition will check negative statement, if title doesn't match and invalid credentials throws error the our page should throw error
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










