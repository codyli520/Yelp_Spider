import scrapy
import datetime
from homework1.items import YelpItem

class YelpSpider(scrapy.Spider):
    name = "yelp"
    id = 0
    start_urls = [
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Los+Angeles,+CA&start=0',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Irvine,+CA&start=0'
    ]

    def parse(self, response):
        for url in response.xpath('//li[@class="regular-search-result"]//span[@class="indexed-biz-name"]/a/@href').extract():
            biz_url = 'https://www.yelp.com/' + url
            yield scrapy.Request(biz_url, callback=self.parse_dir_contents)

        next_url = response.xpath('//div[@class="search-pagination"]//a[contains(@class,"next")]/@href').extract()
        if next_url:
            next_url = 'https://www.yelp.com/' + next_url[0]
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_dir_contents(self, response):
        if response.xpath('//div[contains(@class,"biz-page-header")]') and\
            response.xpath('//div[contains(@class,"biz-page-subheader")]'):

            self.id += 1
            item = YelpItem()
            item['doc_id'] = self.id
            item['url'] = response.url
            item['raw_content'] = response.body
            item['timestamp_crawl'] = datetime.datetime.now()
            yield item
        