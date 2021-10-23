import scrapy
from scrapy import Selector


"""
https://www.ygdy8.net/html/gndy/china/index.html
https://www.ygdy8.net/html/gndy/oumei/index.html
https://www.ygdy8.net/html/tv/hytv/index.html
https://www.ygdy8.net/html/tv/rihantv/index.html
https://www.ygdy8.net/html/tv/oumeitv/index.html
https://www.ygdy8.net/html/zongyi2013/index.html
https://www.ygdy8.net/html/2009zongyi/index.html
https://www.ygdy8.net/html/dongman/index.html
https://www.ygdy8.net/html/gndy/jddy/20160320/50510.html
"""

class Dytt8alexSpider(scrapy.Spider):
    """

    """
    name = 'dytt8alex'
    allowed_domains = ['ygdy8.net']
    base_urls = 'https://ygdy8.net'
    # start_urls = [
    #     'https://www.ygdy8.net/html/gndy/china/index.html',
    #     'https://www.ygdy8.net/html/gndy/oumei/index.html',
    #     'https://www.ygdy8.net/html/tv/hytv/index.html',
    #     'https://www.ygdy8.net/html/tv/rihantv/index.html',
    #     'https://www.ygdy8.net/html/tv/oumeitv/index.html',
    #     'https://www.ygdy8.net/html/zongyi2013/index.html',
    #     'https://www.ygdy8.net/html/2009zongyi/index.html',
    #     'https://www.ygdy8.net/html/dongman/index.html',
    #     'https://www.ygdy8.net/html/gndy/jddy/20160320/50510.html'
    # ]
    start_urls = [
        'https://www.ygdy8.net/html/gndy/china/index.html'
    ]

    def parse(self, response):
        """
        注意这里传入了一个response
        """
        titles = response.css('a[class="ulink"]')
        for i in titles:
            self.logger.debug(i.xpath('@href').extract_first())
            detail_url = self.base_urls + i.xpath('@href').extract_first()
            if detail_url not in self.start_urls:
                yield scrapy.Request(url=detail_url, callback=self.detail_parse)
        print("*" * 40)
        next_url = response.xpath('//div[@class="co_content8"]/div[@class="x"]//a[contains(text(), "下一页")]/@href').extract_first()
        print("next_url = ", next_url)
        # print("response.url", response.url)
        print("*" * 40)
        if next_url:
            # print("yield开始")
            # url = "https://www.ygdy8.net/html/gndy/china/" + next_url
            arry_url = response.url.split('/')
            true_url = ''
            for i in range(len(arry_url)-1):
                true_url = true_url + arry_url[i] + '/'
            true_url = true_url + next_url
            print("true_url = ", true_url)
            yield scrapy.Request(url=url,callback=self.parse)

    def detail_parse(self, response):
        """
        处理详情页
        """
        print("#" * 40)
        self.logger.debug(response.url)
        print("#" * 40)
