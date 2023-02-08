import scrapy
from ..items import KabKotaItem

class SnpmbSpider(scrapy.Spider):
    name = "snpmb"

    def start_requests(self):
        urls = ['https://snpmb.bppp.kemdikbud.go.id/kuotasnmptn.php']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        counter = 0
        data = {}
        for meta in response.xpath('//meta'):
            if (counter % 3 == 0): data['Kode_Kab'] = meta.xpath('@content').get()
            if (counter % 3 == 1): data['Nama_Kab'] = meta.xpath('@content').get()
            if (counter % 3 == 2): data['Master_Kab'] = meta.xpath('@content').get()

            counter = counter + 1
            if (counter == 3):
                yield KabKotaItem(
                    master_kab = data['Master_Kab'],
                    kode_kab = data['Kode_Kab'],
                    nama_kab = data['Nama_Kab']
                )

                #reset counter and data
                data = {}
                counter = 0