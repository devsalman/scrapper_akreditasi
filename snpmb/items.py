# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KabKotaItem(scrapy.Item):
    kode_kab = scrapy.Field()
    nama_kab = scrapy.Field()
    master_kab = scrapy.Field()
