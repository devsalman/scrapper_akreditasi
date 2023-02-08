import scrapy
import csv
import json
import datetime
from ..items import SchoolDetailItem

class SchoolDetailSpider(scrapy.Spider):
    name = 'school_detail'

    def start_requests(self):
        filepath = 'C:\\Users\\devsa\\Downloads\\district_final.csv'
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) #skip header row
            for row in reader:
                kabkota = {
                    'city_code': row[3],
                    'city_name': row[4],
                    'province_name': row[2],
                    'province_code': row[1],
                    'snpmb_kabkota_code': row[5] if (len(row[5]) >= 6) else ('0' + row[5])
                }

                url = 'https://asia-southeast2-pdss-snmptn-299114.cloudfunctions.net/g_func_kuota_kabko?kabko=' + kabkota['snpmb_kabkota_code']
                yield scrapy.Request(url, callback=self.parse, cb_kwargs={'kabkota':kabkota})

    def parse(self, response, kabkota):
        json_data = json.loads(response.text)

        for index,data in json_data.items():
            yield SchoolDetailItem (
                id = int(data['npsn']),
                npsn_s = data['npsn'],
                jenjang_s = 'SMA',
                province_code_i = kabkota['province_code'],
                province_name_s = kabkota['province_name'],
                city_code_i = kabkota['city_code'],
                city_name_s = kabkota['city_name'],
                school_t = data['nama sekolah'],
                akreditasi_s = data['akreditasi'],
                tahun_akreditasi_i = int(datetime.datetime.strptime(data['tanggal kadaluarsa'], '%Y-%m-%d %H:%M:%S').strftime('%Y')) - 5 if (len(data['tanggal kadaluarsa']) > 0) else 0
            )