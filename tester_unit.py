import unittest
from WolleScrapper import *


data={'DMC':'Natura XL','Drops':['Safran','Baby Merino Mix'],'Hahn':'Alpacca Speciale','Stylecraft':'Special DK','Durable':'Coral'}
url="https://www.wollplatz.de/"


class Testunit(unittest.TestCase):
    def test_init(self):
        added=Data(data)

        # check if key elements are found and added correctly
        self.assertIsNotNone(added.datas)
        for a in added.datas:
            self.assertIn(a[0],data," data is missing")

        self.assertIsInstance(get_soup(url),BeautifulSoup," bs4 could not get initiated")

        scrap = Scraper(url)

        # if not brand links, then problem
        links=scrap.data_links()
        self.assertTrue(len(links)>0,"brand links are empty")


        # if not description links, then problem
        descr_links=scrap.get_descr_a_links()

        self.assertTrue(len(descr_links)>0,"description links are empty")

        details={}
        # now for the details
        for descr_link in descr_links:
            self.assertIs(len(descr_link),2,"size list descr_link is not 2")
            for link in descr_link[1]:
                r = GetDetails(link)

                starke = r.get_from_table("Nadelstärke")
                zsm = r.get_from_table("Zusammenstellung")
                avail = r.is_available("Lieferbar")
                price = r.get_price()

                print(avail,price,starke,zsm)
                details[descr_link[0]]=[avail,price,starke,zsm]

        if len(details)!=len(descr_links):
            print("not as many details were founds as description links ")

if __name__ == '__main__':
    unittest
