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

    data_frame['date'] = today
    data_frame['card_urls'] = card_urls

    data_frame['Market Price'] = data_frame['Market Price'].str.replace('$','',regex=False)
    data_frame['Market Price'] = data_frame['Market Price'].str.replace('—','',regex=False)
    data_frame['Market Price'] = data_frame['Market Price'].str.replace(',','',regex=False)
    data_frame['Market Price'] = pd.to_numeric(data_frame['Market Price']) 
    data_frame = data_frame.rename(columns={'Market Price':'market_price_in_dollars'})

    data_frame = data_frame[['card_urls','date','market_price_in_dollars']]

    if i == 0:
        output_df = data_frame
    else:
        output_df = output_df.append(data_frame)

print('Done!')
print(len(output_df))

my_file = Path("data\\pkmn_tcg_stockmarket_prices.csv")
if my_file.is_file():
    previous_data = pd.read_csv('data\\pkmn_tcg_stockmarket_prices.csv')
    #previous_data = previous_data.loc[previous_data['date'] != today]

    output_df = output_df.append(previous_data, ignore_index=True)

output_df.to_csv('data\\pkmn_tcg_stockmarket_prices.csv', index=False)

