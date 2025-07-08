import time

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_customer:
    lnk_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customer_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_Add_customer_xpath = "//a[@class='btn btn-primary']"

    txt_email_xpath = "//*[@id='Email']"
    txt_psswrd_name = "Password"
    txt_first_name_id = "FirstName"
    txt_lastname_id = "LastName"
    rd_btn_gender_male_xpath = "//label[@for='Gender_Male']"
    rd_btn_gender_female_xpath = "//label[@for='Gender_Female']"
    txt_company_name_id = "Company"
    txt_customer_role_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--focus']//ul[@class='select2-selection__rendered']"
    lst_item_registered_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-p83k-3']"
    lst_item_guests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-7aso-4']"
    lst_item_vendor_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-5c1r-5']"
    lst_item_admin_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-o1l5-1']"
    dropdown_managerofvendor_id = "VendorId"
    btn_save_xpath = "//button[@name='save']"
    txt_admincontent_xpath = "//textarea[@id='AdminComment']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def click_on_customer_menu_item(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_item_xpath).click()

    def click_on_add_customer_button(self):
        self.driver.find_element(By.XPATH, self.btn_Add_customer_xpath).click()

    def set_user_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_user_password(self, usr_password):
        self.driver.find_element(By.NAME, self.txt_psswrd_name).send_keys(usr_password)

    def set_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_role_xpath).click()
        time.sleep(3)

        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_admin_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_registered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lst_item_vendor_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.lst_item_registered_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH,self.lst_item_guests_xpath)
        else :
            self.listitem = self.driver.find_element(By.XPATH,self.lst_item_guests_xpath)

        self.driver.execute_script("arguments[0].click();",self.listitem)

    def set_Gender (self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rd_btn_gender_male_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rd_btn_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_btn_gender_female_xpath).click()

    def set_Company_Name(self,companyname):
        self.driver.find_element(By.ID,self.txt_company_name_id).send_keys(companyname)

    def set_Managerofvendor(self,value):
        mgrvendor=Select(self.driver.find_element(By.NAME,self.dropdown_managerofvendor_id))
        mgrvendor.select_by_visible_text(value)

    def save_button(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()

