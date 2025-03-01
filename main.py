import os
import pandas as pd
from dotenv import load_dotenv
from pokemon_api import fetch_pokemon_cards  

# Load Pokemon TCG Developer API Key
load_dotenv()
api_key = os.getenv("TCG_API_KEY")

if not api_key:
    raise ValueError("TCG_API_KEY is missing! Make sure to set it in your .env file.")

# Finds early sets (Base and Gym Heroes)
vintage_queries = ["set.id:base*", "set.id:gym*"]

# Find all cards from Sword & Shield + Scarlet & Violet eras
modern_queries = ["set.id:swsh*", "set.id:sv*"]

# Function to fetch cards data and save it in the folder 'data/'
def fetch_and_save_cards(queries, filename):
    dfs = [fetch_pokemon_cards(api_key, query) for query in queries]
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(f"data/{filename}", encoding='utf-8', index=False)
    print(f"Saved {filename} with {len(combined_df)} cards.")

# Fetch and save vintage and modern cards
fetch_and_save_cards(vintage_queries, "vintage_pkmn_cards_mar2025.csv")
fetch_and_save_cards(modern_queries, "modern_pkmn_cards_mar2025.csv")
