# **Pokémon TCG Stock Market 📈**

A **data visualisation project** that analyses the resale prices of **Pokémon Trading Cards** via the Pokémon TCG API.


[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/pokemon_tcg_stockmarket.svg)](https://github.com/wjsutton/pokemon_tcg_stockmarket/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/pokemon_tcg_stockmarket.svg)](https://github.com/wjsutton/pokemon_tcg_stockmarket/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:


<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

## **:a: About**

Interest in Pokemon trading cards has resurged since their initial release 25 years ago, you can see more on this here: [What's all the hype about Pokémon Trading Cards?](https://public.tableau.com/app/profile/wjsutton/viz/PokemonTradingCardPrices/Dashboard1)

The aim of this project is to produce a datasource of daily prices of Pokemon Trading Cards.

---

## **📊 How It Works**

### **🔄 Data Pipeline**

The project **fetches live market prices** for Pokémon Trading Cards from [**TCGPlayer.com**](https://www.tcgplayer.com/) using their API.

🛠️ **Two Python scripts** handle data collection and processing:

1️⃣ [`pokemon_api.py`](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/pokemon_api.py)
- Defines functions to **fetch Pokémon card data** (one card or multiple) from the API.
- Supports **pagination** to retrieve all available cards.
- Formats the data into a **structured DataFrame**.

2️⃣ [`main.py`](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/main.py)
- Uses `pokemon_api.py` to fetch **vintage** and **modern** card data.
- Saves the data as CSV files:  
  📝 `data/vintage_pkmn_cards_feb2025.csv` (Base & Gym Heroes sets)  
  📝 `data/modern_pkmn_cards_feb2025.csv` (Sword & Shield + Scarlet & Violet sets)

---

## **⚙️ Setup & Installation**

### **1️⃣ Get an API Key**

1. Sign up for a **TCG Developer Account** at 👉 [https://pokemontcg.io/](https://pokemontcg.io/)
2. Retrieve your **API Key** and save it for later.

### **2️⃣ Clone the Repository**

```sh
git clone https://github.com/wjsutton/pokemon_tcg_stockmarket.git
cd pokemon_tcg_stockmarket
``` 

### **3️⃣ Set Up a Virtual Environment**

A virtual environment isolates all python packages to the folder you are working on, and prevents any conflict in existing python packages you have installed. 

```sh
python -m venv venv 
``` 

#### Activate the virtual environment:

Windows:

```sh
venv\Scripts\activate
```

Mac/Linux:

```sh
source venv/bin/activate
```

### **4️⃣ Install Required Packages**

```sh
pip install -r requirements.txt
```

### **5️⃣ Store Your API Key (Environment Variables)**

Create a .env file in the project root directory and add:

```
TCG_API_KEY=your_api_key_here
```

---

## **🚀 Running the Scripts**
Fetch Market Prices

```sh
python main.py
```

Generates updated CSV files with Pokémon card prices and metadata for vintage and modern Pokémon card sets.

### Multiple Cards: **fetch_pokemon_cards(api_key: str, search_query: str)**

    Fetches Pokémon card data based on the given search query with pagination and formats it into a DataFrame.
    
    Parameters:
    - api_key (str): The API key for authentication.
    - search_query (str): The search query to filter cards.
    
    Returns:
    - pd.DataFrame: A DataFrame containing all card details.

**api_key** retrieved from your .env file using the code 

```python
from dotenv import load_dotenv

# Load Pokemon TCG Developer API Key
load_dotenv()
api_key = os.getenv("TCG_API_KEY")
```

**search_query** a code for retrieving a range of pokemon cards, details can be found here: https://docs.pokemontcg.io/api-reference/cards/search-cards

In example, `"set.id:base*"` will return all sets that id start with "base", details of all sets can be found using the API call: https://api.pokemontcg.io/v2/sets via the browser.


### Single Card: **fetch_pokemon_card(api_key: str, card_id: str)**

    Fetches details of a Pokémon TCG card and returns the data as a DataFrame.
    
    Parameters:
    card_id (str): The ID of the Pokémon card.
    api_key (str): The API key for authentication.
    
    Returns:
    pd.DataFrame: A DataFrame containing the card details.

**api_key** retrieved from your .env file using the code 

```python
from dotenv import load_dotenv

# Load Pokemon TCG Developer API Key
load_dotenv()
api_key = os.getenv("TCG_API_KEY")
```

**card_id** the unique identifier for the pokemon card, it usually follows the format: `"Set ID" + "-" + "Card Number from Set"`

In example, `"base1-1"` will return Alakazam, the first card from Base Set. 