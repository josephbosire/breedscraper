__author__ = 'josephbosire'
import scrapy
from breedscraper.items import BreedscraperItem

SOURCE = "petfinder"
class AkcSpider(scrapy.Spider):
    """
    Harvests dog breed information from the akc(American Kernel Club)
    """
    name = "petfinder"
    allowed_domains = ["petfinder.com"]
    start_urls = ["https://www.petfinder.com/dog-breeds/?see-all=1"]

    def parse(self, response):
        for item in response.xpath('//div[@class="breed"]'):
            breed = BreedscraperItem()
            breed['name'] = item.xpath('a[2]/h3/text()').extract()
            breed['description'] = [ desc.replace('\n', '').replace('\r', '').replace("...", "").replace('"",', "") for desc in item.xpath('p/text()').extract()]
            breed['image_urls'] = item.xpath('a[1]/img/@src').extract()
            breed['source'] = SOURCE
            yield breed