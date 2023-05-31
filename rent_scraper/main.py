from yad2_rent_scraper import scrape
from make_csv import write_to_csv
import pandas as pd
import time


if __name__ == "__main__":
    #scrape()
    start_time = time.time()
    write_to_csv()
    seconds = time.time() - start_time
    mins = seconds/60
    hours = mins/60
    print(seconds, mins, hours)