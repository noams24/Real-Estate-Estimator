import json
import re
import base64
import email
import sys
import io
import aiohttp
import asyncio
from urllib.parse import parse_qs, urlencode, urlparse
import requests
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
YAD_2_SEARCH_URL = 'https://gw.yad2.co.il/feed-search-legacy/realestate/forsale'
YAD_2_UNIT_URL = 'https://gw.yad2.co.il/feed-search-legacy/item'

def _get_unit_metadata(link):
    query = parse_qs(urlparse(link).query)
    query['forceLdLoad'] = True

    page = 0
    last_page = None
    units_metadata = set()
    #while page != last_page:
    for page in range(1799):
        #print(page)
        try:
            query['page'] = page

            #print(f'GET {YAD_2_SEARCH_URL}?{urlencode(query)}', file=sys.stderr)
            res = requests.get(YAD_2_SEARCH_URL, params=query).json()
            last_page = res['data']['pagination']['last_page']
            total_items = res['data']['pagination']['total_items']

            for item in res['data']['feed']['feed_items']:
                if 'id' not in item:
                    continue

                metadata = (item['id'], item['abovePrice'])
                if metadata in units_metadata:
                    continue
                
                units_metadata.add(metadata)
        except:
            pass
                
        #break

    print(f'{len(units_metadata)} units found', file=sys.stderr)
    return list(units_metadata)

def _get_unit_data(url):
    try:
        resp = requests.session().get(url)
        resp_json = resp.json()
        #print(f'Received response for url {url}', file=sys.stderr)
        return resp_json['data']
    except:
        return None

def _get_all_unit_data(units_metadata):
    units = []

    #with aiohttp.ClientSession() as session:
    
    for [id, _] in units_metadata:
        url = f'{YAD_2_UNIT_URL}?token={id}'
        new_data = _get_unit_data(url)
        if new_data:
            units.append(new_data)
        #print(_get_unit_data(url))
        #print(f'GET {url}', file=sys.stderr)
      #tasks.append(asyncio.ensure_future(_get_unit_data(session, url)))

    #responses = await asyncio.gather(*tasks)
    #for i, resp in enumerate(responses):
      #resp['abovePrice'] = units_metadata[i][1]
      #units.append(resp)

    return units

def _extract_unit_data(unit):
    items = { item['key']: item['value'] for item in unit['additional_info_items_v2'] }
    info_items = { item['key']: item['value'] for item in unit['important_info_items'] }

    return {
    'city': unit['city_text'],
    'neighborhood': unit['neighborhood'],
    'house type': unit['main_title'].split('&nbsp')[0],
    'house_area': unit['square_meters'],
    'garden_area': unit['garden_area'],
    'rooms': unit['analytics_items']['rooms'],
    'balconies': unit['balconies'],
    'air_condition': unit['analytics_items']['air_conditioner'] ,
    'parking': 1 if unit['parking'].isdigit() else 0,
    'protected_room': unit['analytics_items']['shelter_room'],
    'elevator': unit['analytics_items']['elevator'],
    'renovated': 1 if items['renovated'] else 0,
    'furniture': unit['analytics_items']['furniture'],
    'accessibility': unit['analytics_items']['handicapped'],
    'bars': unit['on_pillars'],
    'storage': unit['analytics_items']['storeroom'],
    'price': int(unit['price'].replace('₪', '').replace(',', '').strip()),
  }


def scrape():
    units_metadata = _get_unit_metadata(YAD_2_SEARCH_URL)

    units = _get_all_unit_data(units_metadata)

    units_data = []
    for unit in units:
        try: 
            units_data.append(_extract_unit_data(unit))
        except Exception as e:
            print(f'Error parsing unit {unit["id"]}', file=sys.stderr)
            print(e, file=sys.stderr)
            continue
        #break

    df = pd.DataFrame(units_data)
    df.to_csv('houses.csv', index=False)


#scrape()

'''
    'city': unit['city_text'],
    'neighborhood': unit['neighborhood'],
    'house type': unit['main_title'].split('&nbsp')[0],
    'house_area': unit['square_meters'],
    'garden_area': unit['garden_area'],
    'rooms': unit['analytics_items']['rooms'],
    'balconies': unit['balconies'],
    'air_condition': unit['analytics_items']['air_conditioner'] != 0,
    'parking': unit['parking'] != '1',
    'protected_room': unit['analytics_items']['shelter_room'],
    'elevator': unit['analytics_items']['elevator'] != 0,
    'renovated': items['renovated'],
    'furniture': unit['analytics_items']['furniture'] != 0,
    'accessibility': unit['analytics_items']['handicapped'] != 0,
    'bars': unit['on_pillars'] != 0,
    'storage': unit['analytics_items']['storeroom'],
    'price': int(unit['price'].replace('₪', '').replace(',', '').strip()),
'''

    #'warhouse': items['warhouse'],
    #'tadiran': items['tadiran_c'],
    #'address_description': unit.get('address_more'),
    #'boiler': items['boiler'],
    #'building_mr': unit['analytics_items']['building_mr'],
    #'floor': unit['analytics_items']['floor'],
    
    
    #'on_pillars': unit['analytics_items']['on_pillars'] != 0,
    
    
    #'area_id': unit['area_id'],
    
    
    #'date_added': unit['date_added'],
    
    #'link': f'https://www.yad2.co.il/item/{unit["id"]}',
    #'info': unit['info_text'],
    #'main_title': unit['main_title'],
    #'longitude': unit['navigation_data']['coordinates']['longitude'],
    #'latitude': unit['navigation_data']['coordinates']['latitude'],
   
    
    
    #'street': unit.get('street'),
    
    #'mediation': 'משרד תיווך' in info_items,
    #'abovePrice': int(unit['abovePrice']),
    #'asset_classification': str(unit['analytics_items'].get('asset_classification'))