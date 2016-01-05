# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base, Source, Breed

class BreedscraperPipeline(object):


    def open_spider(self, spider):
        engine = create_engine('postgresql://projects:projects@localhost:5432/projects')
        # Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        source = self.session.query(Source).filter_by(name=item['source']).first()
        if not source:
            new_source = Source(name=item['source'])
            self.session.add(new_source)
            self.session.commit()
            source = new_source
        breed = Breed(name=item['name'][0], description=item['description'][0], source_avatar=item['image_urls'][0], local_avatar=item['images'][0]['path'], source=source)
        self.session.add(breed)
        self.session.commit()
        return item
