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
hoprStakeAbi = "ABI/HoprStake.json"
hoprBoostAbi = "ABI/HoprBoost.json"

usdtAddress = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
usdcAddress = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
daiAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
hoprAddress= "0xF5581dFeFD8Fb0e4aeC526bE659CFaB1f8c781dA"

xDaiHoprDistributorAddress = "0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66"
xDaiHoprMsAddress = "0x5E1c4e7004B7411bA27Dc354330fab31147DFeF1"
xDaiHoprStakeAddress = "0x912F4d6607160256787a2AD40dA098Ac2aFE57AC"
xDaiHoprBoostAddress = "0x43d13D7B83607F14335cF2cB75E87dA369D056c7"
xDaiXhoprAddress = "0xD057604A14982FE8D88c5fC25Aac3267eA142a08"
xDaiWxhoprAddress = "0xD4fdec44DB9D44B8f2b6d529620f9C0C7066A2c1"

mainNetHoprDistributorAddress = "0xB413a589ec21Cc1FEc27d1175105a47628676552"
mainNetHoprMsAddress = "0x4F50Ab4e931289344a57f2fe4bBd10546a6fdC17"

web3 = Web3(Web3.WebsocketProvider(infuraWS))
# web3 = Web3(Web3.HTTPProvider(infuraHTTP))
# web3 = Web3(Web3.WebsocketProvider(xDaiWS))

print(web3.isConnected())

abiErc20 = json.load(open(erc20abi))
abiHoprDistributor = json.load(open(hoprDistributorAbi))
abiGnosisWallet = json.load(open(gnosisWalletAbi))
abiHoprStake = json.load(open(hoprStakeAbi))
abiHoprBoost = json.load(open(hoprBoostAbi))

usdt = web3.eth.contract(address = usdtAddress, abi = abiErc20)
usdc = web3.eth.contract(address = usdcAddress, abi = abiErc20)
dai = web3.eth.contract(address = daiAddress, abi = abiErc20)
hopr = web3.eth.contract(address = hoprAddress, abi = abiErc20)
xhopr = web3.eth.contract(address = xDaiXhoprAddress, abi = abiErc20)
wxhopr = web3.eth.contract(address = xDaiWxhoprAddress, abi = abiErc20)
xDaiHoprDistributor = web3.eth.contract(address = xDaiHoprDistributorAddress, abi = abiHoprDistributor)
xDaiHoprMs = web3.eth.contract(address = xDaiHoprMsAddress, abi = abiGnosisWallet)
xDaiHoprStake = web3.eth.contract(address = xDaiHoprStakeAddress, abi = abiHoprStake)
xDaiHoprBoost = web3.eth.contract(address= xDaiHoprBoostAddress, abi = abiHoprBoost)

mainNetDistributor = web3.eth.contract(address = mainNetHoprDistributorAddress, abi = abiHoprDistributor)
mainNetHoprMs = web3.eth.contract(address = mainNetHoprMsAddress, abi = abiGnosisWallet)
# end of setup



# sending ERC20 transactions
# `erc20.send` function call
def transfer(recipient, amount, decimals, token):
    return token.encodeABI("transfer", args=[recipient, amount * 10 ** decimals])

# print(transfer("0x8f7a2AbbC8741572427e3426538cD516A41102f3", 10000, 18, hopr))



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
#p1 = mainNetDistributor.encodeABI("revokeAccount", args=["0x8b90b067d02132fC7c5cDf64b8cac04D55aBC2B2", "EarlyTokenBuyers"])
#p2 = mainNetDistributor.encodeABI("addSchedule", args=[[15901200, 31536000, 47437200], [333333, 333333, 333334], "EarlyTokenBuyers2"])
#p3 = mainNetDistributor.encodeABI("addAllocations", args=[["0xc08dE9d8834B3ee012D684dB239bF7868c818327"], [1963929428930000000000000], "EarlyTokenBuyers2"])
#p4 = mainNetDistributor.encodeABI("addAllocations", args=[["0xe3DB7B04c5B761a38a5D46adF68f5C213048c1Ae"], [1052279000000000000000000], "EarlyTokenBuyers"])
#p5 = xDaiHoprBoost.encodeABI("grantRole", args=["0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6", "0xD7682Ef1180f5Fc496CF6981e4854738a57c593E"])

#print("main: " + mainNetHoprMsAddress + " , payload: " + mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, p1]))
#print("main: " + mainNetHoprMsAddress + " , payload: " + mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, p2]))
#print("main: " + mainNetHoprMsAddress + " , payload: " + mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, p3]))
#print("main: " + mainNetHoprMsAddress + " , payload: " + mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, p4]))
#print("main: " + mainNetHoprMsAddress + " , payload: " + mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, transfer("0x960cC811e5eF36760f5c679AF90e821B10385e04", 2897, 6, usdt)]))
#print("xDAI: " + xDaiHoprMsAddress + " , payload: " + xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiHoprBoostAddress, 0, p5]))

#print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdtAddress, 0, transfer("0x054f9541B0b24A49F9dac8e2CeFd59dBeC58dACA", 20000, 6, usdt)]))
#print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdtAddress, 0, transfer("0xB6750624367fF6Cd307338a3d21FF0AA6BD80190", 80000, 6, usdt)]))
#print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdtAddress, 0, transfer("0xCcf17BCA3311C556c74354Eb3B66099574799e7e", 80000, 6, usdt)]))

# print(xDaiHoprMs.encodeABI("revokeConfirmation", args=[64]))

mainSafeAddress = "0x752af2Bf9DbBC1105a83D2CA1eE8F1046D85B702"
print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdtAddress, 0, transfer(mainSafeAddress, 60000, 6, usdt)]))

print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdcAddress, 0, transfer(mainSafeAddress, 60000, 6, usdc)]))

print(mainNetHoprMs.encodeABI("submitTransaction", args=[daiAddress, 0, transfer(mainSafeAddress, 10000, 18, dai)]))

xdaiSafeAddress = "0xE9131488563776DE7FEa238d6112c5dA46be9a9F"
print(xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiHoprBoostAddress, 0, xDaiHoprBoost.encodeABI("grantRole", args=["0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6", xdaiSafeAddress])]))

print(xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiXhoprAddress, 0, transfer(xdaiSafeAddress, 300000, 18, xhopr)]))
