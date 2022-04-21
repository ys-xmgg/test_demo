# def base_page class封装基础操作 
from selenium import webdriver


class BasePage:
    # 构造函数
    def init(self, driver):
        self.driver = driver
        #driver = webdriver.chorme()
    # visit url

    def open(self, url):
        self.driver.get(url)
    # 定位元素
    def locator(self,type):
        self.driver.getby('xpath')
        #//input[@name='accounts]或者绝对位置，input元素[]条件为@input属性
        #$x('----') jQuery选择XXX元素的
    # 输入
    # 点击
