import toml
from utils import run, retry, jsonArg, intToCurrency
config = toml.load('./config.toml')

privateIncentivePremine = 200000000000
airdropsPremine = 200000000000
marketPremine = 1000000000000
commercialApplicationsPremine = 200000000000
teamHoldingPremine = 400000000000

def premine():
    ram_funds = 100000
    retry(config['cleos']['path'] + 'system newaccount --transfer eosio eosio.priv %s --stake-net "%s" --stake-cpu "%s" --buy-ram "%s"' % 
            (config['accounts']['priv_incentive_public_key'], intToCurrency(privateIncentivePremine - ram_funds / 2), intToCurrency(privateIncentivePremine - ram_funds / 2), intToCurrency(ram_funds)))
    retry(config['cleos']['path'] + 'system newaccount --transfer eosio eosio.team %s --stake-net "%s" --stake-cpu "%s" --buy-ram "%s"   ' % 
            (config['accounts']['team_holding_public_key'], intToCurrency(teamHoldingPremine - ram_funds / 2), intToCurrency(teamHoldingPremine  - ram_funds / 2), intToCurrency(ram_funds)))
    retry(config['cleos']['path'] + 'system newaccount --transfer eosio eosio.market %s --stake-net "%s" --stake-cpu "%s" --buy-ram "%s"   ' % 
            (config['accounts']['market_public_key'], intToCurrency(marketPremine - ram_funds / 2), intToCurrency(marketPremine  - ram_funds / 2), intToCurrency(ram_funds)))
    
    retry(config['cleos']['path'] + 'transfer eosio eosio.app "%s"     ' %  (intToCurrency(commercialApplicationsPremine)))
    retry(config['cleos']['path'] + 'transfer eosio eosio.adrop "%s"     ' %  (intToCurrency(airdropsPremine)))

if __name__ == '__main__':
    premine()