# Description
Python script that will query an account to retrieve position and pricing data.

# Execution
Make sure virtualenv is installed and the client is running

1. Create the virtualenv

`virtualenv env`

2. Activate the virtual environment

`source env/bin/activate`

3. Install requirements in the virtual environment

`pip3 install -r requirements.txt`

4. Query

`python3 run.py`

### Help
```
python3 run.py --help
usage: run.py [-h] [--cusip CUSIP] config

positional arguments:
  config         the configuration file with endpoints

optional arguments:
  -h, --help     show this help message and exit
  --cusip CUSIP  the identifier of the security to query for
  ```
--cusip is optional and will allow filtering of results. If not provided it will return all results

### Example
```
python3 run.py config.txt --cusip 912796SG5
{
  "user_id": 99999999,
  "username": "username",
  "authenticated": true,
  "selectedAccount": "CB8008156",
  "portfolio": [
    {
      "cusip": "912796SG5",
      "issueDate": "2019-07-03",
      "maturityDate": "2019-07-03",
      "marketPrice": 99.74700165,
      "marketValue": 14962.05,
      "position": 15.0,
      "parValue": 1000.0,
      "posAtPar": 15000.0
    }
  ]
}
```

## Contact Us
Fluidity is a financial technology company based in Brooklyn, New York, on a mission to rebuild finance using blockchain technology. Reach us at team@fluidity.io for any inquiries related to this repository, the Tokenized Asset Portfolio (TAP), or working with our team.
