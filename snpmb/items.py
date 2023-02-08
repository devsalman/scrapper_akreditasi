# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KabKotaItem(scrapy.Item):
    kode_kab = scrapy.Field()
    nama_kab = scrapy.Field()
    master_kab = scrapy.Field()

# TODO: Create item for school detail data
class SchoolDetailItem(scrapy.Item):
    id = scrapy.Field()
    npsn_s = scrapy.Field()
    jenjang_s = scrapy.Field()
    province_code_i = scrapy.Field()
    province_name_s = scrapy.Field()
    city_code_i = scrapy.Field()
    city_name_s = scrapy.Field()
    school_t = scrapy.Field()
    akreditasi_s = scrapy.Field()
    tahun_akreditasi_i = scrapy.Field()
