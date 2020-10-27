from  LyyPackage.MyCommonLib import CommonShare
import time

class Public(CommonShare):
    #登陆函数
    def login(self,user,pwd):
        self.open_url("http://wewopa.natapp4.cc/jinxiaocun/login.do")
        self.input_data('xpath','//input[@name="account"]',user)
        self.input_data('xpath','//input[@name="password"]',pwd)
        #点击登录
        self.click('xpath','//input[@value="登陆"]')

    #登陆、点击子菜单函数
    def public(self,*args):
        if len(args[2]) != 0 and len(args[3]) != 0:
            self.login(args[2],args[3])
        # 点击子菜单
        str3 = '//a[@headerindex="' + args[0] + '"]'
        self.click('xpath', str3)
        self.click('text', args[1])
        # 进子窗口
        self.stf("mainiFrame")

    # name为数字的定位输入函数（列表）
    def public2(self,*args):
        for i in range(0,len(args)):
            self.input_data('name', str(i+1), args[i])

    # name为数字以外的定位输入函数（字典）
    def public3(self,**args):
        for k,v in args.items():
            self.input_data('name', k, v)

    # 选择时间和输入备注
    def time_remark(self,str1,remark):
        #点击时间输入框
        self.click('name', str1)
        # 返回顶层窗口
        self.stdc()
        # 进入时间子窗口
        ele = self.locateElement('css', "body > div:nth-child(3) > iframe")
        self.stf(ele)
        # 点选今天时间
        self.click('id', 'dpTodayInput')
        #判断有无备注内容传入，有则输入
        if len(remark) != 0:
            self.stdc()
            self.stf("mainiFrame")
            self.input_data('name', 'remark', remark)

    # 月份定天数，然后修改时间
    def time2(self,n):
        times = time.strftime("%Y-%m-%d", time.localtime())
        month = int(times[-5:-3])
        if month == 2:
            if int(times[:3]) % 4 == 0 and int(times[:3]) % 100 != 0 or int(times[:3]) % 400 == 0:
                m = 29
            else:
                m = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            m = 30
        else:
            m = 31
        str1 = ''
        if int(times[-2:]) < m:
            for i in range(1, int(n[1]) + 1):
                if n[0] == '-' and int(times[-2:]) > 0:
                    str1 = str(int(times[-2:]) - i)
                else:
                    str1 = str(int(times[-2:]) + i)
                if int(str1) >= m:
                    break
        return (str(times[:-2]) + str1)

    # 获取页面的列表集合
    def list1(self,str1):
        res1 = self.locateElement('xpaths', str1)
        res = []
        for i in range(1, len(res1)):
            res.append(res1[i].text)
        return res

    def quit(self):
        self.driver.quit()


