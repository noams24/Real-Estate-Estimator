from bs4 import BeautifulSoup
import requests
from get_links_ad import get_all_links
from scrap_ad import get_price, get_non_binary_attributes, get_binary_attributes


class Apartment:
    def __init__(self, city, neighborhood, price, house_type, house_area, garden_area, rooms, balconies, air_condition,
                 parking, protected_room, elevator, sun_balcony, renovated, furniture, accessibility, bars, storage):
        self.city = city
        self.neighborhood = neighborhood
        self.house_type = house_type
        self.price = price
        self.house_area = house_area
        self.garden_area = garden_area
        self.rooms = rooms
        self.balconies = balconies
        self.air_condition = air_condition
        self.parking = parking
        self.protected_room = protected_room
        self.elevator = elevator
        self.sun_balcony = sun_balcony
        self.renovated = renovated
        self.furniture = furniture
        self.accessibility = accessibility
        self.bars = bars
        self.storage = storage

    def __str__(self):
        return str(self.city) + '\n' + str(self.neighborhood) + '\n' + str(self.price) + '\n' + str(
                self.house_type) + '\n' + str(self.house_area) + '\n' + str(self.garden_area) + '\n' + \
                str(self.rooms) + '\n' + str(self.balconies) + '\n' + str(self.air_condition) + '\n' + \
                str(self.parking) + '\n' + str(self.protected_room) + '\n' + str(self.elevator) + '\n' + \
                str(self.sun_balcony) + '\n' + str(self.renovated) + '\n' + str(self.furniture) + '\n' + \
                str(self.accessibility) + '\n' + str(self.bars) + '\n' + str(self.storage)


# constructs apartment object
def make_apartment(apartment_link):
    html_text = requests.get(apartment_link).text
    soup = BeautifulSoup(html_text, "lxml")

    binary_attributes = get_binary_attributes(soup)
    furniture = binary_attributes['furniture']
    air_condition = binary_attributes['air condition']
    parking = binary_attributes['parking']
    protected_room = binary_attributes['protected room']
    accessibility = binary_attributes['accessibility']
    bars = binary_attributes['bars']
    elevator = binary_attributes['elevator']
    storage = binary_attributes['storage']
    sun_balcony = binary_attributes['sun balcony']
    renovated = binary_attributes['renovated']

    non_binary_attributes = get_non_binary_attributes(soup)
    house_type = non_binary_attributes.get('פרטי הנכס').replace('\'', '') if non_binary_attributes.get('פרטי הנכס') is not None else "אין"
    city = non_binary_attributes.get('עיר')
    neighborhood = non_binary_attributes.get('שכונה') if non_binary_attributes.get('שכונה') is not None else "אין"
    rooms = non_binary_attributes.get('חדרים') if non_binary_attributes.get('חדרים') is not None else 0
    house_area = non_binary_attributes.get('שטח בנוי') if non_binary_attributes.get('שטח בנוי') is not None else 0
    garden_area = non_binary_attributes.get('שטח גינה') if non_binary_attributes.get('שטח גינה') is not None else 0
    balconies = non_binary_attributes.get('מרפסות') if non_binary_attributes.get('מרפסות') is not None else 0

    price = get_price(soup)

    return Apartment(city, neighborhood, price, house_type, house_area, garden_area, rooms, balconies, air_condition,
                     parking, protected_room, elevator, sun_balcony, renovated, furniture, accessibility, bars, storage)


# return all the apartments objects
def get_data():
    apartments_links = get_all_links()
    apartments = []

    for apartment_link in apartments_links:
        new_apartment = make_apartment(apartment_link)
        apartments.append(new_apartment)

    return apartments
