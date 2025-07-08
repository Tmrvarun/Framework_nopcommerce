from selenium import webdriver
from Framework.PageObjectModel.Loginpage import Login
from Framework.PageObjectModel.Add_customer_pom import Add_customer
from Framework.PageObjectModel.Search_customer import Customer_search
from Framework.utilities.readproperties import read_config

class search_firstname_01():
    url=read_config.get_app_url()
    username=read_config.get_username()
    password=read_config.get_password()

    def search_firstname(self,setup):
        self.driver=setup()
        self.driver.get(self.url)


        self.lp3=Login(self.driver)  #   This is the object to login using username password and click login button page function
        self.driver.get(self.username)
        self.driver.get(self.password)
        self.lp3.click_login()

        self.addcustomer1=Add_customer(self.driver)#   This is the object to click customer menu and customer menu item page function
        self.addcustomer1.click_on_customer_menu_item()
        self.addcustomer1.click_on_customer_menu()

        self.search_name=Customer_search(self.driver)
        self.search_name.search_firstname("Steve")
        self.search_name.search_lastname("Gates")
        self.search_name.search_button()
        status=self.search_name.row_name_search("Steve Gates") #    This line will pass name to pom function and verify the name , if assert return is true then it will pass else it will fail
        assert True==status
