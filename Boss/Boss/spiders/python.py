import scrapy
from .. import items


class PythonSpider(scrapy.Spider):
    name = 'python'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://login.zhipin.com/?ka=header-login']

    def parse(self, response):
        # 获取列表
        el_list = response.xpath('//div[@class="job-list"]//ul[1]//li')
        for el in el_list:
            item = items.BossItem()
            item["name"] = el.xpath('.//span[@class="job-name"]//a//text()').extract_first()
            item["name_link"] = 'https://www.zhipin.com' + el.xpath('.//span[@class="job-name"]//a//@href').extract_first()
            item["address"] = el.xpath('.//span[@class="job-area"]//text()').extract_first()
            item["salary"] = el.xpath('.//div[@class="job-limit clearfix"]//span[@class="red"]//text()').extract_first()
            item["company"] = el.xpath('.//div[@class="company-text"]//h3[@class="name"]//a//text()').extract_first()
            yield item

        is_next = response.xpath(".//a[@ka='page-next']//@class").extract_first()
        print("is_next", is_next)
        if (is_next == "next disabled"):
            self.crawler.engine.close_spider(self, '停止爬虫!')
        else:
            next_url = "https://www.zhipin.com"+response.xpath(".//a[@ka='page-next']//@href").extract_first()
            print("next_url", next_url)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)



