import scrapy
import json



class ZenodoSpider(scrapy.Spider):
    name = "zenodo"
    allowed_domains = ["zenodo.org"]
    start_urls = ["https://zenodo.org/api/records/?page=1&size=10&communities=oswec&sort=mostrecent"]

    def parse(self, response):
        data = json.loads(response.body)
        #yield each link as a request

       # print(data['hits']['hits'][0]['links']['self'])
        data_list = data['hits']['hits']
        for data in data_list:
           yield  (data['links']['self'])

def run_scrapy_command():

    print("Scheduler started")
    os.system("scrapy runspider zenodo.py -o zenodo.json")

schedule.every(10).seconds.do(run_scrapy_command)
while True:
   # print("Scheduler running")
    schedule.run_pending()
    time.sleep(1)






