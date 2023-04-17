import schedule

import subprocess
import time
from zenodo import ZenodoSpider

def run_spider():
    print ("Running spider")
    command = "scrapy runspider zenodo.py -o output.json"
    subprocess.run(command, shell=True)

schedule.every(7).days.do(run_spider)


while True:
    schedule.run_pending()
    time.sleep(1)


