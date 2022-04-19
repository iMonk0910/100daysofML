import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

with open('jiohtml.txt', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

product_name = []
product_link =[]
product_price = []
product_final_price = []
discount_rate = []


def page_output(URL):

    response = requests.get(URL)
    urlinfo = response.content
    soup1 = BeautifulSoup(urlinfo, 'html.parser')


    ti = soup1.find('div', class_="title-section")
    titl = ti.select('h1')[0].text.strip()


    prdinf = soup1.find_all("table", class_="prodDetTable")


    detail1 = prdinf[0].select('a')
    bn = detail1[0].text.strip()

    mn = prdinf[0].select('td')[1].text.strip()

    detail2_0 = prdinf[1].select('td')
    c_o = str(detail2_0[0].text).strip()

    detail2_1 = prdinf[1].select('span')
    fdtyp = str(detail2_1).partition('-')[2].rpartition('"')[0]

    pr = soup1.find("div", class_="rating-content")
    pro_rat = pr.text[1:4] +'(' + pr.text[5:].strip()+')'


    crn_em = soup1.find('h3', text ='Customer Care Number & Email:').next_sibling.text.strip()
    crn_em_formated = crn_em.split()
    crn = crn_em_formated[0]
    e_m = crn_em_formated[1]




    ad_i = soup1.find(attrs={"class" : "content_txt","id" :"third_desc"}).text
    ad_inf = ''

    for letter in ad_i:
        if letter.isupper():
            ad_inf = ad_inf +' '

        ad_inf += letter

    single_page_output = []

    single_page_output = [titl, pro_rat, fdtyp, bn, mn, crn, e_m, c_o, ad_inf]


    return  single_page_output

links = soup.find_all("a", class_= "category_name prod-name")

print(len(links))
half_link1 = "https://www.jiomart.com/"


prs = soup.find_all("span", class_="price-box")
dis = soup.find_all("span", class_="dis_section")

product_price = []

for i in range(20):
    pr = prs[i].text.partition(': â‚¹ ')[2].strip()
    product_price.append(pr)
    fpr = prs[i].text.rpartition(' M.')[0].partition('â‚¹ ')[2]
    product_final_price.append(fpr)

    discount0 = dis[i].text
    discount1 = discount0.rpartition(' of')[0]
    discount = discount1.strip()
    discount_rate.append(discount)



for i in links:
    a = str(i)
    x = a.partition('href="/')[2]
    half_link2 = x.rpartition('" title=')[0]
    link = half_link1 + half_link2
    product_link.append(link)

jio_mart_sunflower_oil = []
for h, _url in enumerate (product_link):
    output_from_single_page = page_output(_url)
    output_from_single_page.insert(1, product_link[h])
    output_from_single_page.insert(4, product_price[h])
    output_from_single_page.insert(5, discount_rate[h])
    output_from_single_page.insert(6, product_final_price[h])
    jio_mart_sunflower_oil.append(output_from_single_page)


data = pd.DataFrame(jio_mart_sunflower_oil)
