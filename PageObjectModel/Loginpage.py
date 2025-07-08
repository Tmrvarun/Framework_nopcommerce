from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    login_button_xpath="//button[@type='submit']"
    link_logout_linktext="//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver): #Constructor which takes driver parameter form test case and sends that driver to this class driver it is invoked autoomatically at the time of execution
                                #To use action methods of this class we use self.driver
        self.driver=driver

    def setUsername(self,username): #Action method for searching and sending username

        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def setpassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()