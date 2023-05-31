import csv
import time
from apartment import get_data

# the names of the columns in the csv file
#head_line = ['city', 'neighborhood', 'house type', 'house_area', 'garden_area', 'rooms', 'balconies',
             #'air_condition', 'parking', 'protected_room', 'elevator', 'sun_balcony', 'renovated', 'furniture',
             #'accessibility', 'bars', 'storage', 'price']
head_line = ['city', 'neighborhood', 'house type', 'house_area', 'garden_area', 'rooms', 'balconies',
             'air_condition', 'parking', 'protected_room', 'elevator', 'renovated', 'furniture',
             'accessibility', 'bars', 'storage', 'price']



# return row to write in the csv file
def get_row(apartment):
    row = [apartment.city, apartment.neighborhood, apartment.house_type, apartment.house_area,
           apartment.garden_area, apartment.rooms, apartment.balconies, apartment.air_condition, apartment.parking,
           #apartment.protected_room, apartment.elevator, apartment.sun_balcony, apartment.renovated, apartment.furniture,
           apartment.protected_room, apartment.elevator, apartment.renovated, apartment.furniture,
           apartment.accessibility, apartment.bars, apartment.storage, apartment.price]
    return row


# writes the apartments data to the csv file
def write_to_csv():
    apartments_data = get_data()

    with open('apartments.csv', "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(head_line)

        for apartment in apartments_data:
            csv_writer.writerow(get_row(apartment))


# measure the run time of the program
#start_time = time.time()
#write_to_csv()
#print(time.time() - start_time, "seconds")