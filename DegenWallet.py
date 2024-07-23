# modify and uncomment the desired section below
# get infura project id and start via:
# python DegenWallet.py e68eab41f9f74d4287e74f038d1ae5bf

from web3 import Web3
import json
import sys

# infuraProjectId = sys.argv[1]

# print("infura project ID from command line parameter: " + infuraProjectId)

# infuraWS = "wss://mainnet.infura.io/ws/v3/" + infuraProjectId
# infuraHTTP = "https://mainnet.infura.io/v3/" + infuraProjectId
# xDaiWS = "wss://rpc.xdaichain.com/wss"
GnosisRPC = "https://rpc.ankr.com/gnosis"

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

xGNOAddress = "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb"

mainNetHoprDistributorAddress = "0xB413a589ec21Cc1FEc27d1175105a47628676552"
mainNetHoprMsAddress = "0x4F50Ab4e931289344a57f2fe4bBd10546a6fdC17"
QMinter = "0xD7682Ef1180f5Fc496CF6981e4854738a57c593E"

web3 = Web3(Web3.HTTPProvider(GnosisRPC))
# web3 = Web3(Web3.WebsocketProvider(infuraWS))
# web3 = Web3(Web3.HTTPProvider(infuraHTTP))
# web3 = Web3(Web3.WebsocketProvider(xDaiWS))

print(f"RPC provider is {'connected' if web3.is_connected() else 'not connected'}")

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
xgno = web3.eth.contract(address = xGNOAddress, abi = abiErc20)
xDaiHoprDistributor = web3.eth.contract(address = xDaiHoprDistributorAddress, abi = abiHoprDistributor)
xDaiHoprMs = web3.eth.contract(address = xDaiHoprMsAddress, abi = abiGnosisWallet)
xDaiHoprStake = web3.eth.contract(address = xDaiHoprStakeAddress, abi = abiHoprStake)
xDaiHoprBoost = web3.eth.contract(address= xDaiHoprBoostAddress, abi = abiHoprBoost)

mainNetDistributor = web3.eth.contract(address = mainNetHoprDistributorAddress, abi = abiHoprDistributor)
mainNetHoprMs = web3.eth.contract(address = mainNetHoprMsAddress, abi = abiGnosisWallet)
# end of setup



"""
# ADDING SCHEDULE TO XDAI DISTRIBUTOR
addSchedulePayload = xDaiHoprDistributor.encodeABI("addSchedule", args=[[1], [1000000], "2021-10"])
print(xDaiHoprMs.encodeABI("submitTransaction", args=["0x987cb736fBfBc4a397Acd06045bf0cD9B9deFe66", 0, addSchedulePayload]))
"""



"""
# ADDING ALLOCATIONS TO XDAI DISTRIBUTOR
recipients = ["0xeFC05B0D0C8bE8D4Cb3a220ef582E9f7E6FBCd00","0x3f4d0a6654c8365B42DcAa8AA92d9034e2A6141f","0x849D046dfb65E7Bd680F5022613c1C8Ae9a52367","0x3c5B25331C30937ac324D3F20Af0CAA70e645588","0x41B20fd647fb2310C5cF2329B6397A7C75Baa84C","0x62Ec589cc2A82816599A7C6f9d145A62D90C17cB","0x6E2a2acC7253d38e0891F439a9815bEd3771E305","0xE4c140a67A3A95913a6E2FcFc6d6434d94C07641","0xe99dc1864b1bea3EFd8b87d5CEc5b7b65ff23379","0xCa9061Ae96f2728259E328AEda513270532FC43d","0xdB5D39414faB620Dd38e5A477AB58320B10F42c9","0xDe5701C91E479888878f9AEbf1DeCc0B10D88cB5"]
amounts = [4781000000000000000000,2789000000000000000000,3985000000000000000000,2789000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000,1554000000000000000000,1196000000000000000000,1196000000000000000000,1196000000000000000000]

addAllocationsPayload = xDaiHoprDistributor.encodeABI("addAllocations", args=[recipients, amounts, "2021-10"])
"""



"""
# CHECKING MULTISIG TRANSACTION
txId = 63
# tx = xDaiHoprMs.functions.transactions(txId).call()
# print(tx)
"""



"""
# ADD MINTER TO HOPR BOOST
newMinter = "0xD7682Ef1180f5Fc496CF6981e4854738a57c593E"
print(xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiHoprBoostAddress, 0, xDaiHoprBoost.encodeABI("grantRole", args=["0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6", newMinter])]))
"""



"""
# ADD MAIN NET DISTRIBUTOR ALLOCATION
newTokenPurchaserAddress = "0xE3Df4318E057A4017D19C423604273267Ecf2C9A"
newTokenPurchaserAmount = 96666667000000000000000000
print(mainNetHoprMs.encodeABI("submitTransaction", args=[mainNetHoprDistributorAddress, 0, mainNetDistributor.encodeABI("addAllocations", args=[[newTokenPurchaserAddress], [newTokenPurchaserAmount], "EarlyTokenBuyers"])]))
"""


# TRANSFER USDC, USDT, DAI
ComSafeGnosis = "0xD9a00176Cf49dFB9cA3Ef61805a2850F45Cb1D05"
amountGNO = 500000000000000000000

print(xDaiHoprMs.encodeABI("submitTransaction", args=[xGNOAddress, 0, xgno.encodeABI("transfer", args=[ComSafeGnosis, amountGNO])]))


"""
# TRANSFER USDC, USDT, DAI
recipient = "0x752af2Bf9DbBC1105a83D2CA1eE8F1046D85B702"
amountUSDC = 475179296270
amountUSDT = 34143796905
amountDAI  = 172344374231153533378848

print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdcAddress, 0, usdc.encodeABI("transfer", args=[recipient, amountUSDC])]))

print(mainNetHoprMs.encodeABI("submitTransaction", args=[usdtAddress, 0, usdt.encodeABI("transfer", args=[recipient, amountUSDT])]))

print(mainNetHoprMs.encodeABI("submitTransaction", args=[daiAddress, 0, dai.encodeABI("transfer", args=[recipient, amountDAI])]))
"""



"""
# TRANSFER OWNERSHIP OF STAKING CONTRACT
newOwner = "0xD7682Ef1180f5Fc496CF6981e4854738a57c593E"

#print(xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiHoprStakeAddress, 0, xDaiHoprStake.encodeABI("transferOwnership", args=[newOwner])]))

print(xDaiHoprMs.encodeABI("submitTransaction", args=[xDaiWxhoprAddress, 0, wxhopr.encodeABI("transfer", args=[newOwner, 50000000000000000000000])]))
"""


