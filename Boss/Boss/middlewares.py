# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
import json
import requests
import base64
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.support.wait import WebDriverWait


class RandomUserAgent(object):
    """设置随机user-agent"""
    def process_resuqest(self, request, spider):
        with open("/Users/apple/PycharmProjects/Boss_copy2/Boss/Boss/user_agent_all.txt") as file:
            user_agent_list = file.readlines()
        user_agent = random.choice(user_agent_list).strip()
        request.headers["User-Agent"] = user_agent


class SeleniumMiddleware(object):
    """用Selenium模拟登录"""

    def process_request(self, request, spider):
        # 判断是否为登录界面
        url = request.url
        if "ka=header-login" in url:
            opt = webdriver.ChromeOptions()
            opt.add_argument("--headless")
            opt.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome("/Users/apple/Desktop/暂时/chromedriver")
            self.driver.implicitly_wait(20)
            self.driver.get(url)

            self.login()

            response = self.get_image(request)

            coordinate_list = self.base64_api(response, 27).split("|")

            self.check(coordinate_list)
            # 判断是否验证成功
            while True:
                text = self.driver.find_elements_by_xpath('//div[@class="geetest_result_tip"]/text()')
                if len(text) == 0:
                    break
                else:
                    response = self.get_image(request)
                    coordinate_list = self.base64_api(response, 27).split("|")
                    self.check(coordinate_list)

            # 点击登录
            self.driver.find_element_by_xpath("//div[@class='sign-form sign-pwd']//button").click()
            time.sleep(2)
            self.driver.get("https://www.zhipin.com/job_detail/")

            # 搜索python岗位
            time.sleep(5)
            self.driver.find_element_by_xpath("//input[@class='ipt-search']").send_keys("python")
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@class='btn btn-search']").click()
            time.sleep(3)
            res = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding="utf8",
                               request=request)
            return res
        else:
            print("分页开始了")
            self.driver.get(url)
            time.sleep(2)
            self.driver.execute_script("scrollTo(1000,100000)")
            time.sleep(3)
            res = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding="utf8",
                               request=request)
            return res



    @staticmethod
    def base64_api(img, typeid):
        """验证图片交给打码平台，返回验证坐标"""
        base64_data = base64.b64encode(img)
        b64 = base64_data.decode()
        data = {"username": "18795874218", "password": "Zhang5909112", "image": b64, "typeid": typeid}
        result = json.loads(requests.post("http://api.ttshitu.com/imageXYPlus", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""

    def login(self):
        """输入账号密码，点击验证"""
        self.driver.find_element_by_name('account')\
            .send_keys("18795874218")
        self.driver.find_element_by_name('password')\
            .send_keys("Zhang5909112")
        self.driver.find_element_by_xpath('//*[@id="pwdVerrifyCode"]/div').click()
        time.sleep(4)

    def get_image(self, request):
        """获取验证码图片"""
        image_url = self.driver.find_element_by_xpath('//div[@class="geetest_item_wrap"]/img').get_attribute("src")
        headers = {"referer": "https://login.zhipin.com/", "User-Agent": request.headers["User-Agent"]}
        response = requests.get(image_url, headers=headers).content
        return response

    def check(self, coordinate_list):
        """点选验证码"""
        action = webdriver.ActionChains(self.driver)
        image = self.driver.find_element_by_xpath('//div[@class="geetest_item_wrap"]/img')
        for coordinate in coordinate_list:
            x, y = coordinate.split(",")
            action.move_to_element_with_offset(image, int(x), int(y))
            action.click()
        action.perform()
        self.driver.find_element_by_xpath('//a[@class="geetest_commit"]//div').click()


class ProxyMiddleware(object):

    def __init__(self, ip):
        self.ip = ip

    @classmethod
    def from_crawler(cls, crawler):
        return cls(ip=crawler.settings.get('PROXIES'))

    def process_request(self, request, spider):
        ip = random.choice(self.ip)
        request.meta['proxy'] = ip







# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BossSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BossDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
