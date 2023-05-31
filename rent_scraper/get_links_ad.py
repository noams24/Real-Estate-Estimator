from bs4 import BeautifulSoup
import requests


# goes to the specified number page
def go_to_page(page_number):
    return "https://www.ad.co.il/nadlanrent?pageindex=" + str(page_number)


# constructs new apartment link from the apartments id
def make_link(apartment_id):
    return "https://www.ad.co.il/ad/" + str(apartment_id)


# return all the apartments links from specific page in the website
def get_apartments_links(page_link="https://www.ad.co.il/nadlanrent?pageindex=1"):
    html_text = requests.get(page_link).text
    soup = BeautifulSoup(html_text, "lxml")
    apartments = soup.find_all("div", class_="card-block")
    
    apartments_links = []
    for apartment in apartments:
        try:
            new_link = make_link(apartment['data-id'])
            apartments_links.append(new_link)
        except:
            pass

    return apartments_links


# return all the apartments links in the website
def get_all_links():
    all_links = []
    for i in range(500, 1500):
        links_on_page = get_apartments_links(go_to_page(i))
        all_links = all_links + links_on_page
    return all_links


#print(get_apartments_links())