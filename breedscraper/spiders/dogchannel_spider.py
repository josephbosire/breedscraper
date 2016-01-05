__author__ = 'josephbosire'
import scrapy
from breedscraper.items import BreedscraperItem

SOURCE = "Dogchannel"
class DogchannelSpider(scrapy.Spider):
    """
    Harvests dog breed information from the akc(American Kernel Club)
    """
    name = "dogchannel"
    allowed_domains = ["dogchannel.com"]
    start_urls = ["http://www.dogchannel.com/dog-breeds/dog-breeds-starting-with-letter-{}.aspx".format(letter)for letter in map(chr, xrange(97, 123))]

    def parse(self, response):
        for item in response.xpath('//table[@class="searchResultItem"]'):
            breed = BreedscraperItem()
            breed['name'] = item.xpath('tr/td[2]/div/h4/a/span/text()').extract()
            breed['description'] = item.xpath('tr/td[2]/div/p[1]/span/text()').extract() + item.xpath('tr/td[2]/div/p[2]/span/text()').extract()
            breed['image_urls'] = item.xpath('tr/td[1]/a/img/@src').extract()
            breed['source'] = SOURCE
            yield breed