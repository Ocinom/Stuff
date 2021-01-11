# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime

class CheckItem:
    def process_item(self, article, spider):
        if not article or len(article.keys()) < 4:
            raise DropItem('Something is missing!')
        return article

class FormatDate:
    def process_item(self, article, spider):
        article['date'] = article['date'][22:37]
        return article