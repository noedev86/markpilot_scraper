from bs4 import BeautifulSoup
import requests



# type of data to be stored in
class Data:
    datas=[]

    def __init__(self,data):
        for d in data:
            if type(data[d]) is list:
                for descr in data[d]:
                    self.datas.append([d,descr])
            else:
                self.datas.append([d,data[d]])



class GetData(Data):
    def __init__(self):
        #would store the data in the class data
        #self.datas.append(----database data---)
        pass


def get_soup(url):
    doc = requests.get(url)
    soup=BeautifulSoup(doc.text, 'html.parser')
    return soup


class Scraper(Data):
    datas_links = {}
    descr_links = []

    # first get the page from a request
    def __init__(self, url):
        self.soup=get_soup(url)
        self.url=url
    # search for specific tag in the page and return a list of found href links
    def get_a_links(self,tag):
        all_a=self.soup.find_all("a")
        # to eliminate all the not wolle, add a filter
        found=[a['href'] for a in all_a if tag in a.text]

        wolle_filtered=[e for e in found if "wolle" in e]
        # if the link is not complete, add the original url to it

        wolle_url_added=[]

        for w_1 in wolle_filtered:
            if not w_1.startswith(self.url):
                wolle_url_added.append(self.url+w_1)
            else:
                wolle_url_added.append(w_1)

        return wolle_url_added

    # with data class list of the inputs details, get all the links
    def data_links(self):
        # get from brand name link to brand page
        for d in self.datas:
            self.datas_links[d[0]]=self.get_a_links(d[0])
        return self.datas_links

    # now get the pages with beautifulsoup and search for the corresponding description links
    def get_descr_a_links(self):
        # get the data links
        self.data_links()

        for b_name,links in self.datas_links.items():

            # get all the descriptions from the brands from the data before
            d_names=[descr[1] for descr in self.datas if b_name is descr[0]]

            if type(links) is list:
                for link in links:
                    self.soup=get_soup(link)
                    for d_name in d_names:
                        found_links=self.get_a_links(d_name)
                        if len(found_links)>0:
                            self.descr_links.append([b_name,found_links])
        return self.descr_links


# new class to search inside the page for different data

class GetDetails:
    def __init__(self,descr_link):
        # first get the soup of the descr link
        self.descr_soup=get_soup(descr_link)

    #if specific text found in the page on a span, then its available --> "Lieferbar" or "Lieferzeit"
    def is_available(self,tag_avail):
        all_spans=self.descr_soup.find_all("span")

        avail=[a for a in all_spans if tag_avail in a.text]

        if len(avail)>0:
            print(avail[0].text)
            return True

        return False

    def get_price(self):
        price=self.descr_soup.find_all("span", {"class": "product-price"})

        if len(price)>0:
            return price[0]['content']
        else:
            return "not_found"

    def get_from_table(self,name):
        name=self.descr_soup.find("td", text=name)
        if name==None:
            return "not_found"
        val=name.find_next_sibling("td").text
        return val



