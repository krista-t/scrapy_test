import schedule

import os


import time





def run_scrapy_command():

    print("Scheduler started")
    # go out one directory and run the scrapy command
    os.chdir("..")
    os.system("scrapy runspider zenodo.py -o output.json")

#schedule.every(10).seconds.do(run_scrapy_command)
while True:
   # print("Scheduler running")
    schedule.run_pending()
    time.sleep(1)

