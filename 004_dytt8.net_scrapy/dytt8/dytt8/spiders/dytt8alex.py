import scrapy


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
    allowed_domains = ['dytt8.net']
    start_urls = ['http://dytt8.net/']

    def parse(self, response):
        """
        注意这里传入了一个response
        """
        # print('*' * 40)
        # print(response.headers)
        # print('*' * 40)
        # print(response.text)
        # self.logger.debug(response.headers)
        # self.logger.debug(response.text)
        self.logger.debug(response.headers)
