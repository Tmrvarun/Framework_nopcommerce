import random
import string

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Framework.PageObjectModel.Loginpage import Login
from Framework.utilities.readproperties import read_config
from Framework.PageObjectModel.Add_customer_pom import Add_customer


class Test_003_add_customer():
    baseurl = read_config.get_app_url()
    username = read_config.get_username()
    password = read_config.get_password()

    @pytest.mark.regression
    def test_addcustom(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lgp1 = Login(self.driver)
        self.lgp1.setpassword(self.password)
        self.lgp1.click_login()

        self.adcustm = Add_customer(self.driver)
        self.adcustm.click_on_customer_menu()
        self.adcustm.click_on_customer_menu_item()
        self.adcustm.click_on_add_customer_button()
        self.email = random_generator() + "@gmail.com" #This line creates a variable email and calls random_generator function
        self.adcustm.set_user_email(self.email)
        self.adcustm.set_user_password("use123")
        self.adcustm.txt_first_name_id("Test user 1")
        self.adcustm.txt_lastname_id("Under test ")
        self.adcustm.set_Gender("Male")
        self.adcustm.set_Company_Name("ABC TESTING QA")
        self.adcustm.set_customer_role("Registered")
        self.adcustm.set_Managerofvendor("Vendor 2")
        self.adcustm.save_button()

        customer_success_message="The new customer has been added successfully." #This code checks the success message validation message when all details are entered in the form correctly and then we press save button
        success_message=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']")
        if customer_success_message in success_message:
            assert True
            self.driver.close()
        else:
            assert False





def random_generator(size=8, chars=string.ascii_lowercase + string.digits): #this method creates a 8 random lower case alphabet characters
    return ''.join(random.choice(chars) for x in range(size))
