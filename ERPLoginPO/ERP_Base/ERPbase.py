# from selenium.webdriver.common.action_chains import ActionChains


class Base():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_url(self):  # 打开网页
        self.driver.get(self.url)

    def find_element(self, *data):  # 获取元素信息  需要注意的是，获取一类的都需要return 返回
        return self.driver.find_element(*data)

    def find_elements(self, *data):  # 获取一组元素
        return self.driver.find_elements(*data)

    def click_element(self, *data):  # 点击
        self.find_element(*data).click()

    def click_elements(self, number, *data):  # 点击一组元素中的某一个
        self.find_elements(*data)[number].click()

    def get_text(self, *data):  # 获取文本信息
        text = self.find_element(*data).text
        return text

    def input_text(self, text, *data):  # 输入文本信息
        test = self.find_element(*data)
        test.clear()  # 先清除
        test.send_keys(text)  # 再输入

    def iframe_number(self, number):  # 根据下标切换iframe
        iframes = self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(iframes[number])

    def iframe_skip(self):  # 跳出iframe 回到默认的上下文
        self.driver.switch_to.default_content()