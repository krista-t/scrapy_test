import schedule

import os
import time

def run_spider():
    command = "scrapy runspider zenodo.py -o output.json"
    os.system(command)


# Schedule the spider to run every 10 seconds
schedule.every(10).seconds.do(run_spider)

# Run the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

