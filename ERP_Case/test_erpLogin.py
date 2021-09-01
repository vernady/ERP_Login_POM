from ERPLoginPO.ERP_Page.erp_login import ERPlogins
import unittest
from ddt import ddt,data,unpack
from selenium import webdriver


@ddt  # 数据驱动 ddt
class Erp_Login(unittest.TestCase):

    @unpack
    @data([0,'130********','123456'],[0,'150********','123456'])
    def test_erplogin(self, num,username,pwd):
        self.driver = webdriver.Chrome()
        admin = ERPlogins(self.driver,'https://erp.test.sixi.com/')
        admin.get_url()#打开网页
        admin.iframe_number(num)
        admin.input_username(username)#输入账号
        admin.input_pwd(pwd)#输入密码




