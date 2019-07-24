import requests
import traceback
import json
import argparse
import configparser
import logging
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
parser = argparse.ArgumentParser()
parser.add_argument("config", help="the configuration file with endpoints")
parser.add_argument("--cusip", help="the identifier of the security to query for")

def api_call(endpoint):
    try:
        r = requests.get(config['PATHS']['BASE_URL'] + endpoint, verify=False)
        r.raise_for_status()
        logging.info(r.json())
        return r.json()
    except Exception as e:
        logging.error(e)
        print(r.json())
        exit()

if __name__ == "__main__":
    args = parser.parse_args()

    config.read(args.config)

    # update if we have been passed cusip arg
    requested_cusips = None
    if(args.cusip):
        requested_cusips = args.cusip.split(',')

    output = {}
    acct_info = api_call(config['PATHS']['PORTFOLIO_ACCOUNTS_ENDPOINT'])
    account_id = acct_info[0]['accountId']

    output['accountId'] = account_id
    portfolio = []
    endpoint = config['PATHS']['PORTFOLIO_ASSETS_ENDPOINT'].replace('account_id', account_id)
    assets = api_call(endpoint)
    for a in assets:
        try:
            cusip = a['bond']['si'][0]['id']

            #check if we are limited to a selected cusips
            if(requested_cusips and cusip not in requested_cusips):
                continue

            asset = {}
            asset["cusip"] = cusip
            asset["issueDate"] = a['bond']['issueDate']
            asset["maturityDate"] = a['bond']['maturityDate']
            asset["marketPrice"] = a['mktPrice']
            asset["marketValue"] = a['mktValue']
            asset['position'] = a['position']
            asset['parValue'] = a['bond']['parValue']
            asset['posAtPar'] = a['position'] * a['bond']['parValue']

            logging.info(json.dumps(asset, indent=2))
            portfolio.append(asset)
        except Exception as e:
            logging.error(e)
            logging.info("a field missing in data provided by client, skipping")

    output['portfolio'] = portfolio
    print(json.dumps(output, indent=2))
