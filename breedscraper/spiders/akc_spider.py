__author__ = 'josephbosire'
import scrapy
from breedscraper.items import BreedscraperItem

SOURCE = "ack"
class AkcSpider(scrapy.Spider):
    """
    Harvests dog breed information from the akc(American Kernel Club)
    """
    name = "akc"
    allowed_domains = ["akc.org"]
    start_urls = ["http://www.akc.org/dog-breeds/?letter={}".format(letter.upper())for letter in map(chr, xrange(97, 123))]

    def parse(self, response):
        for item in response.xpath('//article[@class="event scale-img-parent"]'):
            breed = BreedscraperItem()
            breed['name'] = item.xpath('div[@class="scale-contents"]/h2/a/text()').extract()
            breed['description'] = item.xpath('div[@class="scale-contents"]/p/text()').extract()
            breed['image_urls'] = ["http:" + url for url in item.xpath('div[@class="scale-img"]/a/img/@src').extract()]
            breed['source'] = SOURCE
            yield breed