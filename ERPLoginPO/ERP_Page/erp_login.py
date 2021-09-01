from ERPLoginPO.ERP_Base.ERPbase import Base # 导入Base类
from selenium.webdriver.common.by import By

class ERPlogins(Base):# 继承Base页中的Base类
    def __init__(self, driver, url):  # 初始化方法
        Base.__init__(self, driver, url)  # 重写父类方法，这里不做改变

    def input_username(self,text):  #输入账号
        self.input_text(text,By.CSS_SELECTOR,'input.ivu-input.ivu-input-large')

    def input_pwd(self, text):  #输入密码
        self.input_text(text, By.CSS_SELECTOR, 'input[placeholder=请输入验证码]')

    def click_end_login(self):  # 点击登录
        self.click_element(By.CSS_SELECTOR,'button[type=button]')

    def get_logins(self):  #获取登录后的文本信息
        return self.get_text(By.CSS_SELECTOR,'span.login-id')