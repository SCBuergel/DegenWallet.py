from web3 import Web3
import json

# DO NOT COMMIT SECRET INFURA PROJECT ID!!!
infuraProjectId = ""

# infuraWS = "wss://mainnet.infura.io/ws/v3/" + infuraProjectId
infuraHTTP = "https://mainnet.infura.io/v3/" + infuraProjectId

erc20abi = "ABI/ERC20.json"
usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# web3 = Web3(Web3.WebsocktProvider(infuraWS))
web3 = Web3(Web3.HTTPProvider(infuraHTTP))

print(web3.isConnected())

abi = json.load(open(erc20abi))

usdt = web3.eth.contract(address = usdtAddress, abi = abi)

# `erc20.send` function call
def transfer(recipient, amount, decimals, token):
    print(token.encodeABI("transfer", args=[recipient, amount * 10 ** decimals]))

transfer("0xB6750624367fF6Cd307338a3d21FF0AA6BD80190", 11681, 6, usdt)


