import scrapy
import json


class ZenodoSpider(scrapy.Spider):
    name = "zenodo"
    allowed_domains = ["zenodo.org"]
    start_urls = ["https://zenodo.org/api/records/?page=1&size=20&access_right=open&communities=oswec"]

    def parse(self, response):
        data = json.loads(response.body)


       # print(data['hits']['hits'][0]['links']['self'])
        data_list = data['hits']['hits']
        for data in data_list:
           yield {'link': data['links']['self']}






