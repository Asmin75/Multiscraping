import scrapy
from scrapy.http.request import Request


class MultiSpider(scrapy.Spider):
    name = 'multiple'
    def start_requests(self):

        with open('urls.txt') as f:
            links = f.readlines()
            links = list(map(lambda x: x.strip(), links))
            for link in links:
                yield Request(link, meta={'start_urls': link}, callback=self.parse)

        # start_urls = links

    def parse(self, response):
        # for url in response.meta['start_urls']:
        #     start_url = url
        start_url = response.meta['start_urls']
        link_list = response.css('ul li a ::text').extract()
        paragraph = response.css('p::text').extract()
        h3 = response.css('h3::text').extract()
        h2 = response.css('h2::text').extract()

        # start_url = list(map(str.strip, start_url))
        # link_list = list(map(str.strip, link_list))
        # paragraph = list(map(str.strip, paragraph))
        # h3 = list(map(str.strip, h3))
        # h2 = list(map(str.strip, h2))

        yield {
            'url': start_url,
            'link_list': link_list,
            'paragraph': paragraph,
            'h3': h3,
            'h2': h2,
        }