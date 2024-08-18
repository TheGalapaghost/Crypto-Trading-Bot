import cbpro
import authcredentials.py
            
sand_url = "https://api-public.sandbox.pro.coinbase.com"
url = 'https://api.pro.coinbase.com/'
client = cbpro.AuthenticatedClient(sand_api_key, sand_api_secret, sand_api_pass, api_url=sand_url)
#client = cbpro.AuthenticatedClient(api_key,api_secret,api_pass, api_url=url)

payment_methods = client.get_payment_methods()
for method in payment_methods:
    currency = method.get('currency', None)
    if currency.upper() == 'USD':
        method_id = method.get('id', None)
    elif(currency is None):
        continue
    
#print(f"Currency is '{currency}'\n")


def get_crypto_balance(crypto_ticker):
    x = client.get_accounts()
    for accounts in x:
        for indies in accounts.values():
            if indies == crypto_ticker:
                print(list(accounts.values())[2])
                
print(client.get_product_historic_rates(product_id='BTC-USD', granularity=900))

#get_crypto_balance('USD')
#get_crypto_balance('BTC')


#client.deposit(amount=5000, currency=currency, payment_method_id=method_id)
#client.place_market_order(product_id='BTC-USD', side='buy', funds='5')

# a = client.get_product_ticker('BTC-USD')

# price = []

# price.append(float(a['price']))

# print(price)















