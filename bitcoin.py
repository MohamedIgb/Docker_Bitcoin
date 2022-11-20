from flask import Flask, render_template
import requests
import redis


app = Flask(__name__)
redis = redis.Redis(host='redis', port=6379)


def getbitcoinPrice():
    bitcoinPrice = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(bitcoinPrice)
    data = response.json()['price']
    redis.set('btcoinPrice', data)
    return data

def getbitcoinAvgPrice():
    bitcoinAvrPrice = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9'
    response = requests.get(bitcoinAvrPrice)
    data = response.json()['Data']['Data']
    avg = 0

    for price in data:
        avg += price['open']

    avg /= 10
    redis.set('btcoinAvgPrice', avg)
    return avg



@app.route("/")
def home():
    return render_template("index.html", price=getbitcoinPrice(), avgPrice=getbitcoinAvgPrice()) 



if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")