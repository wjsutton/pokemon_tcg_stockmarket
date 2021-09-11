import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from pathlib import Path

today = date.today()

pack_df = pd.read_csv('data\\pkmn_tcg_packs.csv')
packs = pack_df['pack']

for i in range(len(packs)):

    pack = packs[i]
    print(pack)

    url = "https://shop.tcgplayer.com/price-guide/pokemon/" + pack
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tbl = soup.find("table")
    data_frame = pd.read_html(str(tbl))[0]
    urls = soup.find_all("div",{"class":"thumbnail"},"a")   

    card_urls = []
    img_urls = []

    for a in urls:
        card = a.select('a')
        card_urls = card_urls + [card[0]['href']]
        image = a.select('img')
        img_urls = img_urls + [image[0]['src']]

    data_frame['pack'] = pack
    data_frame['card_urls'] = card_urls
    data_frame['img_urls'] = img_urls
    data_frame['img_urls'] = data_frame['img_urls'].str.replace('_25w','')
    data_frame['img_urls'] = 'https://product-images.tcgplayer.com/' + data_frame['img_urls'].str.extract('(\d+)') + '.jpg'

    data_frame = data_frame[['card_urls','PRODUCT','Rarity','pack','img_urls']]

    if i == 0:
        output_df = data_frame
    else:
        output_df = output_df.append(data_frame)

print('Done!')
print(len(output_df))

output_df.to_csv('data\\pkmn_tcg_stockmarket_metadata.csv', index=False)

