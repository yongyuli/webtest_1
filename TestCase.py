from LyyPackage.Example import Public
import unittest
from selenium.webdriver.support.select import Select
import time
import random
import warnings

class Test(unittest.TestCase):
    def setUp(self):
        print("===== Start =====")
        # 去除警告提示
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        print("====== End ======")

    #登录的测试用例
    def test_001(self):
        print("测试是否登陆成功")
        log = Public()
        try:
            log.login('admin8', "admin")
            # 获取用户名前缀'Welcome'
            data = str(log.get_text('xpath', '//div[@class="right_header"]')).split(" ")[0]
            # 断言判断是否登录成功
            self.assertEqual('Welcome', data, msg="登录未成功")
        finally:
            log.quit()

    # 反向测试
    # # 只输入账号的情况
    def test_002(self):
        print("测试不输入账号的情况")
        log = Public()
        try:
            log.login('', "admin")
            self.assertEqual("F", log.xsdd('//div[@class="right_header"]'), msg="已输入账号！")
        finally:
            log.quit()

    # # 只输入密码的情况
    def test_003(self):
        print("测试不输入密码的情况")
        log = Public()
        try:
            log.login('admin8', "")
            self.assertNotEqual("T", log.xsdd('//div[@class="right_header"]'), msg="已输入密码！")
        finally:
            log.quit()

    # # 订购产品
    def test_004(self):
        print("测试订购产品")
        log = Public()
        try:
            log.public('0h', '订购产品', 'admin8', 'admin')
            #输入内容
            log.public2('1','3','2','1','5')
            log.time_remark('orderTime','test')
            #提交
            log.click('xpath', '//input[@id="button"]')
            data = log.get_text('css','body > div:nth-child(1)')
            self.assertEqual('添加订单成功', data, msg="订购产品不成功")
        finally:
            log.quit()

    # # 库存查询
    def test_005(self):
        print("测试库存查询")
        log = Public()
        try:
            log.public('2h','库存查询','admin8', 'admin')
            #选择搜素站点
            scobj = Select(log.locateElement('id', 'sName'))
            time.sleep(2)
            scobj.select_by_index(random.randint(0,len(scobj.options)))
            log.click('xpath','//input[@value="查询"]')
            self.assertEqual("T", log.xsdd('//*[@id="rounded-corner"]/tbody/tr[6]'), msg="查询无结果！")
        finally:
            log.quit()

    # 添加网点
    def test_006(self):
        print("测试添加网点")
        log = Public()
        try:
            log.public('2h', '网点管理', 'admin8', 'admin')
            log.click('xpath','//*[@id="rounded-corner"]/tbody/tr[2]/td/a')
            str1 = 'ytest'
            log.input_data('name','shopName',str1)
            log.input_data('name','shopBz','ytestm')
            log.click('name','button1')
            self.assertIn(str1 , log.list1('//*[@id="rounded-corner"]/tbody/tr/td[2]') ,msg="添加网点失败！")
        finally:
            log.quit()

    # 出库管理
    # # 产品出库
    def test_007(self):
        print("测试产品出库")
        log = Public()
        try:
            log.public('3h', '产品出库', 'admin8', 'admin')
            scobj = Select(log.locateElement('name', 'shopid'))
            time.sleep(2)
            scobj.select_by_index(random.randint(0, len(scobj.options)))
            # 输入内容
            log.public2('1', '3', '2', '1', '5')
            log.time_remark('outtime','test')
            # 提交
            log.click('xpath', '//input[@value="确认出库"]')
            data = log.get_text('css', 'body')
            self.assertEqual('产品出库成功', data, msg="产品出库失败！")
        finally:
            log.quit()

    # 入库记录查询
    def test_008(self):
        print("测试入库记录查询")
        log = Public()
        try:
            log.public('1h', '入库记录查询', 'admin8', 'admin')
            time1 = log.time2('-2')
            time2 = log.time2('+3')
            log.input_data('name','starttime',time1)
            log.input_data('name','endtime',time2)
            # 提交
            log.click('xpath', '//input[@value="查询"]')
            #查询列表
            self.assertNotEqual('[]', log.list1('//*[@id="rounded-corner"]/tbody/tr'),msg="入库记录查询失败！")
        finally:
            log.quit()

    # 员工信息
    # 添加员工
    def test_009(self):
        print("测试添加员工")
        log = Public()
        try:
            log.public('4h', '添加员工', 'admin8', 'admin')
            log.public3(name='小明1',phone='1008610000',address='guangxi',birthday='2020-10-20',price='10000',note='test')
            #选择性别
            log.click('xpath','//input[@id="sex0"]')
            #确认
            log.click('xpath', '//input[@name="button"]')
            data = log.get_text('css', 'body')
            self.assertEqual('成功', data, msg="添加员工失败！")
        finally:
            log.quit()

    # 删除员工
    def test_010(self):
        print("测试删除员工")
        log = Public()
        try:
            log.public('4h', '员工管理', 'admin8', 'admin')
            # 通过定位获取要删除的对象在列表的第几个进行拼接语句删除
            str1 = '小明1'
            str2 = []
            res = log.list1('//*[@id="rounded-corner"]/tbody/tr/td[1]')
            for i in range(0,len(res)):
                if res[i] == str1:
                    str2.append('//*[@id="rounded-corner"]/tbody/tr[' + str(i+2) + ']/td[7]/a')
            for i in str2:
                log.click('xpath',i)
                log.click('xpath','//span[@class="yes"]')
                self.assertNotIn(str1, log.list1('//*[@id="rounded-corner"]/tbody/tr/td[1]'),msg="删除员工失败！")
        finally:
            log.quit()

    # 客户管理
    # # 新增客户
    def test_011(self):
        print("测试新增客户")
        log = Public()
        try:
            log.public('5h', '客户管理', 'admin8', 'admin')
            log.click('xpath','//*[@id="rounded-corner"]/tbody/tr[2]/td/a')
            str1 = '小李'
            log.public3(name=str1,phone='10086',address='gx',remark='test')
            log.click('xpath', '//input[@value="确认添加"]')
            self.assertIn(str1, log.list1('/html/body/table/tbody/tr/td[1]'), msg="新增客户失败！")
        finally:
            log.quit()
    # # 编辑客户信息
    def test_012(self):
        print("测试编辑客户信息")
        log = Public()
        try:
            log.public('5h', '客户管理', 'admin8', 'admin')
            str1 = '小李'
            str2 = []
            res = log.list1('/html/body/table/tbody/tr/td[1]')
            for i in range(0, len(res)):
                if res[i] == str1:
                    str2.append('/html/body/table/tbody/tr[' + str(i + 2) + ']')
            for i in str2:
                log.click('xpath',i + '/td[5]/a')
                s1 = log.list1(i)
                log.public3(phone='10000',remark='y修改了')
                log.click('xpath', '//input[@value="确认修改"]')
                s2 = log.list1(i)
                self.assertIsNot(s1, s2, msg="修改客户信息失败！")
        finally:
            log.quit()
    # # 删除客户
    def test_013(self):
        print("测试删除客户")
        log = Public()
        try:
            log.public('5h', '客户管理', 'admin8', 'admin')
            str1 = '小李'
            str2 = []
            res = log.list1('/html/body/table/tbody/tr/td[1]')
            for i in range(0,len(res)):
                if res[i] == str1:
                    str2.append('/html/body/table/tbody/tr[' + str(i+2) + ']/td[6]')
            for i in str2:
                log.click('xpath',i)
                log.click('xpath','//span[@class="yes"]')
                self.assertNotIn(str1, log.list1('/html/body/table/tbody/tr/td[1]'), msg="删除客户失败！")
        finally:
            log.quit()

    #系统设置
    # # 添加管理员
    def test_014(self):
        print("测试添加管理员")
        log = Public()
        try:
            log.public('6h', '添加管理员', 'admin8', 'admin')
            # 注：用户名不可与已有的重复
            log.public3(account='小明C',password='10010',password2='10010',name='admin',note='test')
            log.click('xpath', '//input[@value="确认添加"]')
            self.assertEqual('成功', log.get_text('xpath','/html/body'), msg="新增客户失败！")
        finally:
            log.quit()

    # 入库管理
    # 产品入库
    @unittest.skip("因产品入库需引用订单编号，而订单记录查询的搜索功能不稳定，查无结果，跳过测试")
    def test_015(self):
        print("测试产品入库")
        log = Public()
        try:
            log.public('0h', '订单记录查询', 'admin8', 'admin')
            time1 = log.time2('-1')
            time2 = log.time2('+1')
            log.input_data('name', 'starttime', time1)
            log.input_data('name', 'endtime', time2)
            # 选择订单状态
            scobj = Select(log.locateElement('name', 'orderstate'))
            time.sleep(1)
            scobj.select_by_index(random.randint(0, len(scobj.options)))
            # 查询
            log.click('xpath', '//input[@value="查询"]')
            # 查询订单编号列表
            res = log.list1('/html/body/table/tbody/tr/td[1]')

            log.stdc()
            log.public('1h', '产品入库')
            num = random.randint(0,len(res))
            log.input_data('name', 'orderid',res[num])
            log.time_remark('intime','')
            log.stdc()
            log.stf("mainiFrame")
            log.input_data('name', 'remark', 'test')
            # 提交
            log.click('xpath', '//input[@name="button1"]')
            data = log.get_text('css', 'body > div')
            self.assertEqual('成功入库', data, msg="失败,请检查订单编号是否有效或者是否已经入库")
        finally:
            log.quit()
