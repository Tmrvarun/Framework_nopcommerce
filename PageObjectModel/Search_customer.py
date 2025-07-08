from selenium import webdriver
from selenium.webdriver.common.by import By


class Customer_search:
    box_email_id = "SearchEmail"
    box_firstname_id = "SearchFirstName"
    box_lastname_id = "SearchLastName"
    btn_search_xpath = "//button[@id='search-customers']"

    table_searchresults = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']/div[1]/div/div/div[2]/div/table"
    table_row_xpath = "//table[@id='customers-grid']/tbody//tr"
    table_column_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self,driver):
        self.driver=driver

    def search_customeremail(self, serachemail):
        self.driver.find_element(By.ID, self.box_email_id).clear()
        self.driver.find_element(By.ID, self.box_email_id).sendkeys(serachemail)

    def search_firstname(self, serachfirstname):
        self.driver.find_element(By.ID, self.box_firstname_id).clear()
        self.driver.find_element(By.ID,self.box_firstname_id).sendkeys(serachfirstname)

    def search_lastname(self,searchlastname):
        self.driver.find_element(By.ID,self.box_lastname_id).clear()
        self.driver.find_element(By.ID,self.box_lastname_id).senkeys(searchlastname)

    def search_button(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def row_count_search(self):
        return len(self.driver.find_element(By.XPATH,self.table_row_xpath))

    def column_count_search(self):
        return len(self.driver.find_element(By.XPATH,self.table_column_xpath))

    def row_email_search(self,email):
        email_flag=False
        for r in range (1 ,self.row_count_search() +1 ):
            table_email=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td [2]").text()
            if table_email==email:
                email_flag=True
                break
            return email_flag

    def row_name_search (self,name):
        name_flag=False
        for r in range (1 , self.row_count_search() +1):
            table_name=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td [3]").text()
            if table_name==name:
                name_flag=True
                break
            return name_flag



