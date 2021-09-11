<h1 style="font-weight:normal">
  Pokemon TCG Stockmarket 📈
</h1>


[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/pokemon_tcg_stockmarket.svg)](https://github.com/wjsutton/pokemon_tcg_stockmarket/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/pokemon_tcg_stockmarket.svg)](https://github.com/wjsutton/pokemon_tcg_stockmarket/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

A dataviz project showing the resale prices of Pokemon trading cards. 

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:


<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

## :a: About

Interest in Pokemon trading cards has resurged since their initial release 25 years ago, you can see more on this here: [What's all the hype about Pokémon Trading Cards?](https://public.tableau.com/app/profile/wjsutton/viz/PokemonTradingCardPrices/Dashboard1)

The aim of this project is to produce a dashboard showing the daily prices of Pokemon trading cards in a stockmarket style.


## :snake: Pipeline

The data is sourced from the [tcgplayer.com](https://www.tcgplayer.com/) website which contains the latest market price for all Pokemon cards in dollars, two python scripts collect the data:
- [python/get_tcg_prices.py](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/python/get_tcg_prices.py) produces a dataset of card_url, date, and market price saved here: [data/pkmn_tcg_stockmarket_prices.csv](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/data/pkmn_tcg_stockmarket_prices.csv)
- [python/refresh_tcg_metadata.py](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/python/refresh_tcg_metadata.py) collects the metadata associated with each card_url: card name, rarity, image_url and saved here: [data/pkmn_tcg_stockmarket_metadata.csv](https://github.com/wjsutton/pokemon_tcg_stockmarket/blob/main/data/pkmn_tcg_stockmarket_metadata.csv)


