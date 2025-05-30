import os
import pandas as pd
from dotenv import load_dotenv
from pokemon_api import fetch_pokemon_cards  
from datetime import datetime

# Load Pokemon TCG Developer API Key
load_dotenv()
api_key = os.getenv("TCG_API_KEY")

if not api_key:
    print("TCG_API_KEY is missing! Make sure to set it in your .env file.")

# Function to fetch cards data and save it in the folder 'data/'
def fetch_and_save_cards(queries, base_filename):
    dfs = [fetch_pokemon_cards(api_key, query) for query in queries]
    combined_df = pd.concat(dfs, ignore_index=True)

    # Add datetime stamp to filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{base_filename.replace('.csv', '')}_{timestamp}.csv"

    os.makedirs("data", exist_ok=True)
    combined_df.to_csv(f"data/{filename}", encoding='utf-8', index=False)

# Finds Base Set
base_set = ["set.id:base*"]

fetch_and_save_cards(base_set, "base_set_pkmn_cards.csv")