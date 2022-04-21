from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.base.base_page import BasePage

#登录页面对象，实现登录测试流
class LoginPage(BasePage):
    url = ''
    #element
    user = (By.Name,'')
    pwd = (by.Xpath)
    #业务流
    def login(self,username,password):
        self.open(self,url)
        self.input(self.user,username)
        self.input(self.pwd,password)
        self.click(self.button)

    ####    下面这部分内容正常在case中
    if __name__ == '--main--':
        driver = webdriver.Chrome()
        user = 'sss'
        pwd = '.git\'
        LoginPage(driver).login(username, password)