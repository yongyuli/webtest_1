from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonShare(object):
    # 构造函数 初始化
    def __init__(self):
        #创建浏览器
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        pass
    # 打开一个网页
    def open_url(self,url):
        self.driver.get(url)
        #设置隐式等待
        self.driver.implicitly_wait(10)
        pass

    # 封装定位
    def locateElement(self,locate_type,value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif  locate_type =="name":
            el = self.driver.find_element_by_name(value)
        elif locate_type == "class":
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == "text":
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == "xpath":
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == "xpaths":
            el = self.driver.find_elements_by_xpath(value)
        elif locate_type == "css":
            el = self.driver.find_element_by_css_selector(value)

        if el is not None:
            return el

    #  封装点击函数
    def click(self,locate_type,value):
        el = self.locateElement(locate_type,value)
        el.click()
        time.sleep(1)

     # 封装输入函数
    def input_data(self,locate_type,value,data):
        el = self.locateElement(locate_type, value)
        el.clear()
        el.send_keys(data)
        time.sleep(1)

    # 先点击 后输入
    def actionChain(self,locate_type,value,data):
        el = self.locateElement(locate_type, value)
        #清除内容
        el.clear()
        # 模拟鼠标事件 先点击 后输入
        ActionChains(self.driver).click(el).send_keys(data).perform()
        time.sleep(2)

    # 判断异常
    def catch(self,value):
        try:
            value
        except Exception:
            return "F"
        else:
            return "T"
            pass
        finally:
            self.driver.quit()

    # 获取链接文本
    def get_text(self,locate_type,value):
        el = self.locateElement(locate_type, value)
        return el.text

    # 进入iframe子窗口
    def stf(self,str):
        self.driver.switch_to.frame(str)

    # 返回顶层窗口
    def stdc(self):
        self.driver.switch_to.default_content()

    #切换标签
    def stw(self,str1,num):
        self.driver.find_element_by_tag_name('body').send_keys(str1)
        self.driver.switch_to.window(self.driver.window_handles[num])

    # 显式等待异常函数
    def xsdd(self,str1):
        try:
            # 1秒内每隔0.2秒去定位，超时或超时定位不到就报异常
            WebDriverWait(self.driver, 1, 0.1).until(EC.presence_of_all_elements_located((By.XPATH, str1)))
        except Exception:
            return "F"
        else:
            return "T"
        finally:
            self.driver.quit()
