# coverts price from string to int
def price_to_int(price_text):
    try:
        price_int = (int(price_text.replace(',', '')))
        return price_int
    except ValueError:
        return 0


# return the price in the soup html
def get_price(soup):
    price_html = soup.find_all("h2", class_="card-title")
    price_text = price_html[1].text.split()[0]
    return price_to_int(price_text)


# return all the non binary attributes in the soup html as dictionary
def get_non_binary_attributes(soup):
    main_table = soup.find("table", class_="table table-sm mb-4")
    rows = main_table.find_all("tr")

    attributes = {}
    for tr in rows:
        tds = tr.find_all("td")
        attr_name = tds[0].text.strip()
        attr = tds[1].text.strip()
        attributes[attr_name] = attr

    return attributes


# return whether div is checked or unchecked
def has_attribute(div):
    if 'disabled' in div['class']:
        return 0
    else:
        return 1


# return all the binary attributes in the soup html as dictionary
def get_binary_attributes(soup):

    main_div = soup.find("div", class_="card-icons flex-wrap d-flex h-100")
    divs = main_div.find_all("div")
    binary_attributes = {'furniture': has_attribute(divs[1]), 'air condition': has_attribute(divs[2]),
                         'parking': has_attribute(divs[3]), 'protected room': has_attribute(divs[4]),
                         'accessibility': has_attribute(divs[6]), 'bars': has_attribute(divs[7]),
                         'elevator': has_attribute(divs[8]), 'storage': has_attribute(divs[9]),
                         'sun balcony': has_attribute(divs[10]), 'renovated': has_attribute(divs[11])}

    return binary_attributes
