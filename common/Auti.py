from selenium import webdriver
import time


class GetXiaoMi:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://item.mi.com/product/10000041.html'

    def login(self):
        try:
            self.driver.get(self.url)
            time.sleep(2)
            home_login_butten = self.driver.find_element_by_xpath(".//*[@id='J_buyBox']/div/div[1]/div/a[1]")
            home_login_butten.click()
            input_username = self.driver.find_element_by_class_name('item_account')
            input_username.clear()
            input_username.send_keys('username')
            input_password = self.driver.find_element_by_id('pwd')
            input_password.clear()
            input_password.send_keys('password')
            login_butten = self.driver.find_element_by_id('login-button')
            login_butten.click()
            assert (self.driver.find_element_by_xpath(".//*[@id='error-outcon']/div/span]"),
                    u"登陆失败，请检查用户名或密码")
        except Exception as e:
            print(e)

    @staticmethod
    def system_time():
        sys_time = time.time()
        return sys_time

    @staticmethod
    def preset_time():
        set_time = '2017-05-12 09:59:55'  # 设置抢购时间，最好提前几秒
        # 将其转换为时间数组
        time_array = time.strptime(set_time, '%Y-%m-%d %H:%M:%S')
        # 转换为时间戳
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def get_xiaomi(self):
        try:
            if self.system_time() >= self.preset_time():
                while True:
                    self.driver.find_element_by_class_name('btn btn-primary btn-biglarge J_proBuyBtn add').click()
                    if self.driver.title == u'你来晚了':
                        print(u'又悲剧了，默默的问候小米~')
                        break
                    else:
                        print(u'<-------------赶紧手动付款吧------------>')
            else:
                print(u'时间设置错误')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    run = GetXiaoMi()
    run.get_xiaomi()
