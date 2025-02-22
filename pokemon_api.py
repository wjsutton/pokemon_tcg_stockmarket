import requests
import pandas as pd

def fetch_pokemon_cards(api_key: str, search_query: str):
    """
    Fetches Pokémon card data based on the given search query with pagination and formats it into a DataFrame.
    
    Parameters:
    - api_key (str): The API key for authentication.
    - search_query (str): The search query to filter cards.
    
    Returns:
    - pd.DataFrame: A DataFrame containing all card details.
    """
    page_num = 1
    page_size = 250  # Max allowed page size
    all_cards = []
    url = 'https://api.pokemontcg.io/v2/cards'
    headers = {'X-Api-Key': api_key}

    while True:
        params = {'q': search_query, 'page': page_num, 'pageSize': page_size}
        response = requests.get(url, headers=headers, params=params)

        # If error return empty dataframe
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return pd.DataFrame() 

        data = response.json()
        
        if 'data' not in data or not isinstance(data['data'], list):
            print("Error: Unexpected response format")
            return pd.DataFrame()

        for card in data["data"]:
            all_cards.append({
                "ID": card["id"],
                "Name": card["name"],
                "Pokedex Number": card.get("nationalPokedexNumbers", [None])[0],
                "Supertype": card.get("supertype", ""),
                "Subtypes": ", ".join(card.get("subtypes", [])),
                "HP": card.get("hp", ""),
                "Types": ", ".join(card.get("types", [])),
                "Attacks": ", ".join([f"{atk['name']} ({atk.get('damage', '0')})" for atk in card.get("attacks", [])]),
                "Weaknesses": ", ".join([f"{w['type']} {w['value']}" for w in card.get("weaknesses", [])]),
                "Retreat Cost": len(card.get("retreatCost", [])),
                "Set Name": card["set"]["name"],
                "Release Date": card["set"].get("releaseDate", ""),
                "Artist": card.get("artist", ""),
                "Rarity": card.get("rarity", ""),
                "Card Image (Small)": card["images"]["small"],
                "Card Image HiRes": card["images"]["large"],
                "TCG Player URL": card.get("tcgplayer", {}).get("url", ""),
                "TCG Price Date": card.get("tcgplayer", {}).get("updatedAt", ""),
                "TCG Market Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("market", ""),
                "TCG Low Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("low", ""),
                "TCG High Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("high", ""),
                "TCG Market Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("market", ""),
                "TCG Low Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("low", ""),
                "TCG High Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("high", ""),
                "TCG Market Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("market", ""),
                "TCG Low Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("low", ""),
                "TCG High Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("high", ""),
            })

        total_cards = data.get('totalCount', len(all_cards))
        
        if len(all_cards) >= total_cards:
            break  # Stop when all cards are fetched

        page_num += 1  # Move to the next page

    return pd.DataFrame(all_cards)

def fetch_pokemon_card(api_key: str, card_id: str) -> pd.DataFrame:
    """
    Fetches details of a Pokémon TCG card and returns the data as a DataFrame.
    
    Parameters:
    card_id (str): The ID of the Pokémon card.
    api_key (str): The API key for authentication.
    
    Returns:
    pd.DataFrame: A DataFrame containing the card details.
    """
    url = f'https://api.pokemontcg.io/v2/cards/{card_id}'
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    all_cards = []
    
    # If error return empty dataframe
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return pd.DataFrame() 

    data = response.json()
    
    if 'data' not in data or not isinstance(data['data'], list):
        print("Error: Unexpected response format")
        return pd.DataFrame()

    for card in data["data"]:
        all_cards.append({
            "ID": card["id"],
            "Name": card["name"],
            "Pokedex Number": card.get("nationalPokedexNumbers", [None])[0],
            "Supertype": card.get("supertype", ""),
            "Subtypes": ", ".join(card.get("subtypes", [])),
            "HP": card.get("hp", ""),
            "Types": ", ".join(card.get("types", [])),
            "Attacks": ", ".join([f"{atk['name']} ({atk.get('damage', '0')})" for atk in card.get("attacks", [])]),
            "Weaknesses": ", ".join([f"{w['type']} {w['value']}" for w in card.get("weaknesses", [])]),
            "Retreat Cost": len(card.get("retreatCost", [])),
            "Set Name": card["set"]["name"],
            "Release Date": card["set"].get("releaseDate", ""),
            "Artist": card.get("artist", ""),
            "Rarity": card.get("rarity", ""),
            "Card Image (Small)": card["images"]["small"],
            "Card Image HiRes": card["images"]["large"],
            "TCG Player URL": card.get("tcgplayer", {}).get("url", ""),
            "TCG Price Date": card.get("tcgplayer", {}).get("updatedAt", ""),
            "TCG Market Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("market", ""),
            "TCG Low Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("low", ""),
            "TCG High Price USD (Normal)": card.get("tcgplayer", {}).get("prices", {}).get("normal", {}).get("high", ""),
            "TCG Market Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("market", ""),
            "TCG Low Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("low", ""),
            "TCG High Price USD (Reverse Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("reverseHolofoil", {}).get("high", ""),
            "TCG Market Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("market", ""),
            "TCG Low Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("low", ""),
            "TCG High Price USD (Holofoil)": card.get("tcgplayer", {}).get("prices", {}).get("holofoil", {}).get("high", ""),
        })

    return pd.DataFrame(all_cards)
