# dca-coinbase

Tiny CLI to place market orders on Coinbase Pro, ideal for DCA.

## Prerequisites
Generate an API key and set the following environment variables `CB_PRO_API`, `CB_PRO_SECRET`, `CB_PRO_PASS` accordingly.

You must also install the required Python package(s):
```
pip install -r requirements.txt
```

## Usage
```
python dca.py [trading_pair] [fiat_spend]
```
Here, `fiat_spend` is the $/£/€/¥/? value you wish to spend.

Set up one/more cron jobs according to your DCA interval needs, for example, place $100 BTC market orders daily at midnight:
```
0 0 * * * python dca.py BTC-USD 100
```
