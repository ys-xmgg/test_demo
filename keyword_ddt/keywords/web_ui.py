# 关键字封装类:定位、点击、输入、等待、切换、悬停、断言
# 定义驱动类
# 构造函数
from selenium import webdriver


class WebDemo:
    # 构造函数
    def __init__(self, driverType):
        self.driver = self.browser(driverType)
    # driver = webdriver.chorme()
    # visit url

    def browser(self, driverType):
        try:
            if driverType == 'Chorme':
                driver = webdriver.Chrome()
            else:
                driver = getattr(webdriver, driverType)
            return driver
        finally:
            return webdriver.Chrome()

    def open(self, url):
        self.driver.get(url)
    # 关闭浏览器

    def quit(self):
        self.driver.quit()
    # 定位元素方式

    def locatorType(self, type):
        self.driver.getby(type)
        # //input[@name='accounts]或者绝对位置，input元素[]条件为@input属性
        # $x('----') jQuery选择XXX元素的

    # 定位by name value

    def locator(self, name, value):
        return self.driver.find_element(name, value)
    # 输入

    def input_txt(self, name, value, txt):
        self.locator(name, value).send_keys(txt)
    # 点击

    def click(self, name, value):
        self.locator(name, value).click()
