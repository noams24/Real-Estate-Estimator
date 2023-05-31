from yad2_sale_scraper import scrape
from make_csv import write_to_csv
import pandas as pd
import time

if __name__ == "__main__":
    start_time = time.time()
    #scrape()
    print(time.time() - start_time, "seconds")
    write_to_csv()

    #df1 = pd.read_csv('houses.csv')
    #df2 = pd.read_csv('apartments.csv')

    #combined_df = pd.concat([df1, df2])
    #combined_df = combined_df.reset_index(drop=True)
    #combined_df.to_csv('tables/sale.csv', index=False)
    seconds = time.time() - start_time
    mins = seconds/60
    hours = mins/60
    print(seconds, mins, hours)

