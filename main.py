from bs4 import BeautifulSoup
import requests



# TODO: get availability, price, nailstrengh, zsmstellung

details={'DMC':'Natura XL','Drops':['Safran','Baby Merino Mix'],'Hahn':'Alpacca Speciale','Stylecraft':'Special double knit'}

url="https://www.wollplatz.de/"
# url="https://www.wollplatz.de/#sqr:(q[dmce])"



# print(sp.prettify())

def get_soup(_url=""):
    if _url=="":
        global url
        _url=url
    doc = requests.get(_url)
    sp= BeautifulSoup(doc.text,'html.parser')
    return sp

def search_atag(tag,url=""):

    soup=get_soup(url)
    if url=="":
        s="a[href*={}]".format(tag.lower())
        selection = soup.select(s)
    else:
        selection=soup.find_all("a")
        selection=soup.find_all(lambda _tag: len(_tag.find_all()) == 0 and tag in _tag.text)

        if len(selection)>0:
            return selection[0]['href']
    for sel in selection:
        # print("found : ",sel)
        if 'href' in sel.attrs:
            return sel['href']


for brand in details:
    descriptions=details[brand]
    link = search_atag(brand)

    if link == None:
        print('brand wasnt found')
        continue
    # if multiple descriptions for same link
    if type(descriptions) is list:
        for descr in descriptions:
            # product brand was found, go to link and search for description
            prod_link=search_atag(descr,link)
            print(prod_link)
            # get specific product page
            prod_page=get_soup(prod_link)
            price=prod_page.find_all("span", {"class": "product-price","itemprop":"price"})
            if len(price)>0:
                # price
                print(price[0]['content'])

            avail=prod_page.find_all("span", {"class": "stock-green"})
            if len(avail)>0:
                print("is available to buy")
            else:
                not_avail=prod_page.find_all("span", {"class": "stock-red"})
                if len(not_avail) > 0:
                    print("is not available to buy")
    # only 1 descr
    else:
        print(descriptions)

        # search brand page to get products of brand
        prod_link=search_atag(descriptions, link)
        if prod_link==None:
            print("description of product wasn't found")
            continue
        # get specific product page
        prod_page=get_soup(prod_link)
        price=prod_page.find_all("span", {"class": "product-price","itemprop":"price"})
        if len(price)>0:
            # price
            print(price[0]['content'])

        avail=prod_page.find_all("span", {"class": "stock-green"})
        if len(avail)>0:
            print("is available to buy")
        else:
            not_avail=prod_page.find_all("span", {"class": "stock-red"})
            if len(not_avail) > 0:
                print("is not available to buy")