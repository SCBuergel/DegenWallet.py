from web3 import Web3
import json

# DO NOT COMMIT SECRET INFURA PROJECT ID!!!
infuraProjectId = "e68eab41f9f74d4287e74f038d1ae5bf"

infuraWS = "wss://mainnet.infura.io/ws/v3/" + infuraProjectId
# infuraHTTP = "https://mainnet.infura.io/v3/" + infuraProjectId
# xDaiWS = "wss://rpc.xdaichain.com/wss"

erc20abi = "ABI/ERC20.json"
hoprDistributorAbi = "ABI/HoprDistributor.json"
gnosisWalletAbi = "ABI/GnosisWallet.json"

usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
usdcAddress = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
daiAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
hoprAddress= "0xF5581dFeFD8Fb0e4aeC526bE659CFaB1f8c781dA"

xDaiHoprDistributorAddress = "0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66"
xDaiHoprMsAddress = "0x5E1c4e7004B7411bA27Dc354330fab31147DFeF1"

mainNetHoprDistributorAddress = "0xB413a589ec21Cc1FEc27d1175105a47628676552"
mainNetHoprMsAddress = "0x4F50Ab4e931289344a57f2fe4bBd10546a6fdC17"

web3 = Web3(Web3.WebsocketProvider(infuraWS))
# web3 = Web3(Web3.HTTPProvider(infuraHTTP))
# web3 = Web3(Web3.WebsocketProvider(xDaiWS))

print(web3.isConnected())

abiErc20 = json.load(open(erc20abi))
abiHoprDistributor = json.load(open(hoprDistributorAbi))
abiGnosisWallet = json.load(open(gnosisWalletAbi))

usdt = web3.eth.contract(address = usdtAddress, abi = abiErc20)
usdc = web3.eth.contract(address = usdcAddress, abi = abiErc20)
dai = web3.eth.contract(address = daiAddress, abi = abiErc20)
hopr = web3.eth.contract(address = hoprAddress, abi = abiErc20)
xDaiHoprDistributor = web3.eth.contract(address = xDaiHoprDistributorAddress, abi = abiHoprDistributor)
xDaiHoprMs = web3.eth.contract(address = xDaiHoprMsAddress, abi = abiGnosisWallet)
# end of setup
mainNetDistributor = web3.eth.contract(address = mainNetHoprDistributorAddress, abi = abiHoprDistributor)
mainNetHoprMs = web3.eth.contract(address = mainNetHoprMsAddress, abi = abiGnosisWallet)



# sending ERC20 transactions
# `erc20.send` function call
def transfer(recipient, amount, decimals, token):
    print(token.encodeABI("transfer", args=[recipient, amount * 10 ** decimals]))

# transfer("0x8f7a2AbbC8741572427e3426538cD516A41102f3", 10000, 18, hopr)



# adding schedule to MS
addSchedulePayload = xDaiHoprDistributor.encodeABI("addSchedule", args=[[1], [1000000], "2021-10"])
# print(xDaiHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, addSchedulePayload]))

# adding allocations to MS
recipients = ["0xeFC05B0D0C8bE8D4Cb3a220ef582E9f7E6FBCd00","0x3f4d0a6654c8365B42DcAa8AA92d9034e2A6141f","0x849D046dfb65E7Bd680F5022613c1C8Ae9a52367","0x3c5B25331C30937ac324D3F20Af0CAA70e645588","0x41B20fd647fb2310C5cF2329B6397A7C75Baa84C","0x62Ec589cc2A82816599A7C6f9d145A62D90C17cB","0x6E2a2acC7253d38e0891F439a9815bEd3771E305","0xE4c140a67A3A95913a6E2FcFc6d6434d94C07641","0xe99dc1864b1bea3EFd8b87d5CEc5b7b65ff23379","0xCa9061Ae96f2728259E328AEda513270532FC43d","0xdB5D39414faB620Dd38e5A477AB58320B10F42c9","0xDe5701C91E479888878f9AEbf1DeCc0B10D88cB5"]
amounts = [4781000000000000000000,2789000000000000000000,3985000000000000000000,2789000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1554000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000]

addAllocationsPayload = xDaiHoprDistributor.encodeABI("addAllocations", args=[recipients, amounts, "2021-10"])
# print(xDaiHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, addAllocationsPayload]))



# checking multisig transactions
txId = 63
# tx = xDaiHoprMs.functions.transactions(txId).call()
# print(tx)

# isConfirmed = xDaiHoprMs.functions.isConfirmed(txId).call()
# print(isConfirmed)

# payload = xDaiHoprMs.encodeABI("executeTransaction", args=[63])
# print(payload)



# revoking account, adding new schedule and two additional allocations
p1 = mainNetDistributor.encodeABI("revokeAccount", args=["0x8b90b067d02132fC7c5cDf64b8cac04D55aBC2B2", "EarlyTokenBuyers"])
p2 = mainNetDistributor.encodeABI("addSchedule", args=[[15901200, 31536000, 47437200], [333333, 333333, 333334], "EarlyTokenBuyers2"])
p3 = mainNetDistributor.encodeABI("addAllocations", args=[["0xc08dE9d8834B3ee012D684dB239bF7868c818327"], [1963929428930000000000000], "EarlyTokenBuyers2"])
p4 = mainNetDistributor.encodeABI("addAllocations", args=[["0xe3DB7B04c5B761a38a5D46adF68f5C213048c1Ae"], [1052279000000000000000000], "EarlyTokenBuyers"])

print(mainNetHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, p1]))
print(mainNetHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, p2]))
print(mainNetHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, p3]))
print(mainNetHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, p4]))

