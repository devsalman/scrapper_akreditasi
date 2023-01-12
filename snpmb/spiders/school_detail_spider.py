import scrapy
import csv
import json
import datetime

class SchoolDetailSpider(scrapy.Spider):
    name = 'school_detail'

    def start_requests(self):
        list_kabkota = []
        filepath = 'C:\\Users\\devsa\\Downloads\\kab_kota.csv'
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) #skip header row
            for row in reader:
                kabkota = {
                    'city_code': row[0],
                    'city_name': row[3],
                    'province_name': row[2],
                    'province_code': row[5],
                    'snpmb_kabkota_code': row[6] if (len(row[6]) >= 6) else ('0' + row[6])
                }

                list_kabkota.append(kabkota)

        data = {'city_code': '1112', 'city_name': 'KABUPATEN ACEH BARAT DAYA', 'province_name': 'ACEH', 'province_code': '11', 'snpmb_kabkota_code': '061700'}
        url = 'https://asia-southeast2-pdss-snmptn-299114.cloudfunctions.net/g_func_kuota_kabko?kabko=' + data['snpmb_kabkota_code']

        yield scrapy.Request(url, callback=self.parse, cb_kwargs={'kabkota':data})

    def parse(self, response, kabkota):
        json_data = json.loads(response.text)
        list_of_school_detail = []
        self.log(response.text)

        for index,data in json_data.items():
            school_detail = {
                'id': int(data['npsn']),
                'npsn_s': data['npsn'],
                'jenjang_s': 'SMA',
                'province_code_i': kabkota['province_code'],
                'province_name_s': kabkota['province_name'],
                'city_code_i': kabkota['city_code'],
                'city_name_s': kabkota['city_name'],
                'school_t': data['nama sekolah'],
                'akreditasi_s': data['akreditasi'],
                'tahun_akreditasi_i': int(datetime.datetime.strptime(data['tanggal kadaluarsa'], '%Y-%m-%d %H:%M:%S').strftime('%Y')) - 5 if (len(data['tanggal kadaluarsa']) > 0) else 0
            }

            self.log(','.join(str(value) for value in school_detail.values()))