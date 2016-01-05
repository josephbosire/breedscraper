import scrapy
class BreedscraperItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    source = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
