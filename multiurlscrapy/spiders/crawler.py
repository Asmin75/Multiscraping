from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(CrawlSpider):
    name = 'my-crawler'
    allowed_domains = ["ntc.net.np", "starternepal.com"]
    start_urls = [l.strip() for l in open('urls.txt').readlines()]

    # def start_requests(self):
    #
    #     with open('urls.txt') as f:
    #         links = f.readlines()
    #         links = list(map(lambda x: x.strip(), links))
    #         for link in links:
    #             yield Request(link, meta={'start_urls': link})

    rules = [
             Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        print('Got response from %s .' % response.url)
        start_url = response.request.url
        # paragraph = response.css('p::text').extract()
        h3 = response.css('h3::text').extract()
        h2 = response.css('h2::text').extract()
        # print('Paragraph: % \n' % paragraph)
        # print('h3: %s \n' % h3)
        # print('h3: %s \n' % h2)

        yield {
            'url': start_url,
            # 'paragraph': paragraph,
            'h3': h3,
            'h2': h2,
        }
