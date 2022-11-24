from WolleScrapper import *

url="https://www.wollplatz.de/"

data={'DMC':'Natura XL','Drops':['Safran','Baby Merino Mix'],'Hahn':'Alpacca Speciale','Stylecraft':'Special DK','Durable':'Coral'}

# first initiate the scraper
# scrap=Scraper(url)
# initiate the data

Data(data)

scrap=Scraper(url)
# s=scrap.get_a_links("DMC")
# r=scrap.data_links()

descr_links=scrap.get_descr_a_links()

for descr_link in descr_links:
    for link in descr_link[1]:
        r=GetDetails(link)
        print(link)
        starke=r.get_from_table("Nadelstärke")
        zsm=r.get_from_table("Zusammenstellung")
        avail=r.is_available("Lieferbar")
        price=r.get_price()

        print(descr_link[0],starke,zsm,avail,price)

exit()

# # other wolle test
# scrap2=Scraper("https://www.fischer-wolle.de/")
#
# data2={'DMC':'Natura XL','Rico':'Alpaca','Lana Grossa':'Cool Wool'}
#
# for d in data2:
#     if type(data2[d]) is list:
#         for descr in data2[d]:
#             e = Data(d, descr)
#     else:
#         e=Data(d,data2[d])
#
# descr_links=scrap2.get_descr_a_links()
#
# for descr_link in descr_links:
#     for link in descr_link[1]:
#         r=GetDetails(link)
#         print(link)
#         starke=r.get_from_table("Nadelstärke")
#         zsm=r.get_from_table("Zusammenstellung")
#         avail=r.is_available("Lieferzeit")
#
#         print(descr_link[0],starke,zsm,avail)