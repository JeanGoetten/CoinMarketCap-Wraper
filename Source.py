from urllib.request import urlopen
import datetime
import json

#insert here your coin name - DEFAULT AS bitcoin
symbol_coin = "bitcoin"

#########################

space = " "
URL = "https://api.coinmarketcap.com/v1/ticker/" + symbol_coin + space + "/"
htmltext = urlopen(URL)
    
data = json.load(htmltext)

for module in data:
    sigla = module['symbol']
    rank  = module['rank']
    price_USD = module['price_usd']
    price_BTC = module['price_btc']
    volume_24h_USD = module['24h_volume_usd']
    market_cap_USD = module['market_cap_usd']
    available_SUPPLY = module['available_supply']
    total_SUPPLY = module['total_supply']
    last_UPDATE  = module['last_updated']

#time converter
last_UPDATE_number = float(last_UPDATE)
format_time = datetime.datetime.fromtimestamp(last_UPDATE_number)

fmt = format_time.strftime('%H:%M:%S %d/%m/%Y')

rank_str  = ("Rank: " + rank)
sigla_str = ("Coin: " + sigla)
price_USD_str = ("Valor dólar: " + price_USD + " USD")
price_BTC_str = ("Valor Bitcoin: " + price_BTC + " BTC")
volume_24h_USD_str  = ("Volume 24h: " + volume_24h_USD + " USD")
market_cap_USD_str  = ("Market Cap 24h: " + market_cap_USD + " USD")
available_SUPPLY_str  = ("Avaiable Supply: " + available_SUPPLY + " Kins")
last_UPDATE_str  = ("Last Update: " + fmt)


lista_de_dados_str = [rank_str, sigla_str, price_USD_str, price_BTC_str,
                      volume_24h_USD_str,market_cap_USD_str, available_SUPPLY_str,
                      last_UPDATE_str]
lista_de_dados     = {'data 24h ' : [
										{
										"rank" : rank, 
										"sigla" : sigla,
										"preço" : price_USD,
										"preço btc" : price_BTC,
										"volume diário" : volume_24h_USD,
                      					"market cap" : market_cap_USD,
                      					"avaiable supply" : available_SUPPLY,
                      					"último update" : last_UPDATE
                      					}
                      				]
                     }



#time title converter
last_UPDATE_number_clean = float(last_UPDATE)
format_time_clean = datetime.datetime.fromtimestamp(last_UPDATE_number_clean)

fmt_clean = format_time_clean.strftime('%Y %m %d  %H %M %S')

#print in json - you need create a DATA/ folder or remove this from comand line
#for save your data ticker in a new folder, release next comand line and setup comment the other one:
#date_file_name = fmt_clean
date_file_name = ""
with open('DATA/' + symbol_coin + date_file_name + '.json' , 'a') as outfile:
    json.dump(lista_de_dados, outfile)
outfile.close()

#print in terminal
print(lista_de_dados)
