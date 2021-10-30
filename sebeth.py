from web3 import Web3
import json

# DO NOT COMMIT SECRET INFURA PROJECT ID!!!
infuraProjectId = ""

# infuraWS = "wss://mainnet.infura.io/ws/v3/" + infuraProjectId
infuraHTTP = "https://mainnet.infura.io/v3/" + infuraProjectId

erc20abi = "ABI/ERC20.json"
hoprDistributorAbi = "ABI/HoprDistributor.json"
gnosisWalletAbi = "ABI/GnosisWallet.json"

usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
usdcAddress = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
daiAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
hoprAddress= "0xF5581dFeFD8Fb0e4aeC526bE659CFaB1f8c781dA"

xDaiHoprDistributorAddress = "0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66"
xDaiHoprMsAddress = "0x5E1c4e7004B7411bA27Dc354330fab31147DFeF1"

# web3 = Web3(Web3.WebsocktProvider(infuraWS))
web3 = Web3(Web3.HTTPProvider(infuraHTTP))

# print(web3.isConnected())

abiErc20 = json.load(open(erc20abi))
abiHoprDistributor = json.load(open(hoprDistributorAbi))
abiGnosisWallet = json.load(open(gnosisWalletAbi))

usdt = web3.eth.contract(address = usdtAddress, abi = abiErc20)
usdc = web3.eth.contract(address = usdcAddress, abi = abiErc20)
dai = web3.eth.contract(address = daiAddress, abi = abiErc20)
hopr = web3.eth.contract(address = hoprAddress, abi = abiErc20)
xDaiHoprDistributor = web3.eth.contract(address = xDaiHoprDistributorAddress, abi = abiHoprDistributor)
xDaiHoprMs = web3.eth.contract(address = xDaiHoprMsAddress, abi = abiGnosisWallet)

# `erc20.send` function call
def transfer(recipient, amount, decimals, token):
    print(token.encodeABI("transfer", args=[recipient, amount * 10 ** decimals]))

# transfer("0x8f7a2AbbC8741572427e3426538cD516A41102f3", 10000, 18, hopr)
addSchedulePayload = xDaiHoprDistributor.encodeABI("addSchedule", args=[[1], [1000000], "2021-10"])
print(xDaiHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, addSchedulePayload]))

recipients = ["0xeFC05B0D0C8bE8D4Cb3a220ef582E9f7E6FBCd00","0x3f4d0a6654c8365B42DcAa8AA92d9034e2A6141f","0x849D046dfb65E7Bd680F5022613c1C8Ae9a52367","0x3c5B25331C30937ac324D3F20Af0CAA70e645588","0x41B20fd647fb2310C5cF2329B6397A7C75Baa84C","0x62Ec589cc2A82816599A7C6f9d145A62D90C17cB","0x6E2a2acC7253d38e0891F439a9815bEd3771E305","0xE4c140a67A3A95913a6E2FcFc6d6434d94C07641","0xe99dc1864b1bea3EFd8b87d5CEc5b7b65ff23379","0xCa9061Ae96f2728259E328AEda513270532FC43d","0xdB5D39414faB620Dd38e5A477AB58320B10F42c9","0xDe5701C91E479888878f9AEbf1DeCc0B10D88cB5"]
amounts = [4781000000000000000000,2789000000000000000000,3985000000000000000000,2789000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1554000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000]

addAllocationsPayload = xDaiHoprDistributor.encodeABI("addAllocations", args=[recipients, amounts, "2021-10"])
print(xDaiHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, addAllocationsPayload]))

