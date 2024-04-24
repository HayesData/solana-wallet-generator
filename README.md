# solana-wallet-generator
Generates Solana wallets and writes to console or csv.

## Installation
Requires Poetry dependency manager https://python-poetry.org/

Clone this repository
``` bash
git clone git@github.com:HayesData/solana-wallet-generator.git
```

Install dependencies
``` bash
poetry install
```

## Usage
There are only two arguments for this script.

- count: sets how many wallets to generate
  - Default = 1
- output: will output to csv formatted file
  - Default = null; which will print to console

#### Usage Examples
``` bash
python wallet-generator.py -c 10 # outputs 10 keypairs to the console

python wallet-generator.py -c 10 -o wallets.csv # outputs generated wallets to file
```
