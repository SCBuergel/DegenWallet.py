# this script reads a private key and attempts to send the entire balance plus half the maximum tx fees to the HOPR DevBank on Gnosis Chain (that should not work and it fails (as expected) with:
# ValueError: {'code': -32010, 'message': 'InsufficientFunds, Account balance: 200158000000000000, cumulative cost: 200258000000000000'}

from web3 import Web3
import json
import sys

# this requires a file called privatekey.hex that contains the private key in the first line of the file. The private key should be hex without `0x` prefix.

with open("privatekey.hex") as f:
    privatekey = f.readline().strip()

#rpcHttp = "https://rpc.ankr.com/gnosis"
rpcHttp = "https://derp.hoprnet.org/rpc/xdai/mainnet"
web3 = Web3(Web3.HTTPProvider(rpcHttp))

account = web3.eth.account.privateKeyToAccount(privatekey)

nonce = web3.eth.getTransactionCount(account.address)

balance = web3.eth.getBalance(account.address)

gas = 100000
gasPrice = 2000000000
value = balance - 100000000000000
#value = 1000000000000000000
print(f"balance: {web3.fromWei(balance,'ether')}")
print(value)
# HOPR DevBank
recipient = "0x2402da10A6172ED018AEEa22CA60EDe1F766655C"
tx = {
    'nonce': nonce,
    'to': recipient,
    'value': value,
    'gas': gas,
    'gasPrice': gasPrice
}

signed_tx = web3.eth.account.signTransaction(tx, privatekey)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))

