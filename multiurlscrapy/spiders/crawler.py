import scrapy
from scrapy.http.request import Request
from ..items import MultiurlscrapyItem

class MultiSpider(scrapy.Spider):
    name = 'multiple'
    # start_urls = [
    #     "https://starternepal.com/",
    #     "https://www.ntc.net.np/"
    # ]
    # def start_requests(self):
    #     with open('urls.txt', 'rb') as urls:
    #         for url in urls:
    #             yield Request(str(url), callback=self.parse)
    #
    # def parse(self, response):
    #     for text in response.css('div'):
    #         item = MultiurlscrapyItem()
    #         item['paragraph'] = text.css("p::text").extract()
    #         yield item
    with open('urls.txt') as f:
        links = f.readlines()
        links = list(map(lambda x: x.strip(), links))
    start_urls = links

    def parse(self, response):
        # for text in response.css('div'):
        paragraph = response.css('p::text').extract()
        paragraph = list(map(str.strip, paragraph))
        yield {
            'paragraph': paragraph,
            # 'Main Info': description,
        }