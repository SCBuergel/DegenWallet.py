# this script reads a private key and attempts to send the entire balance plus 1 wei in tx fees to the HOPR DevBank on Gnosis Chain (that should not work but it does not fail)

from web3 import Web3
import json
import sys

# this requires a file called privatekey.hex that contains the private key in the first line of the file. The private key should be hex without `0x` prefix.

with open("privatekey.hex") as f:
    privatekey = f.readline().strip()

rpcHttp = "https://rpc.gnosischain.com"
#rpcHttp = "https://derp.hoprnet.org/rpc/xdai/mainnet"
web3 = Web3(Web3.HTTPProvider(rpcHttp))

account = web3.eth.account.privateKeyToAccount(privatekey)

nonce = web3.eth.getTransactionCount(account.address)

balance = web3.eth.getBalance(account.address)

gas = 100000
gasFeePerGas = 2000000000
maxPriorityFeePerGas = 1000000000
value = balance - 199999999999999

print(f"nonce: {nonce}")
print(f"balance: {web3.fromWei(balance,'ether')}")

# HOPR DevBank
recipient = "0x2402da10A6172ED018AEEa22CA60EDe1F766655C"
tx = {
    'nonce': nonce,
    'to': recipient,
    'value': value,
    'gas': gas,
    'maxFeePerGas': gasFeePerGas,
    'maxPriorityFeePerGas': maxPriorityFeePerGas,
    'chainId': 100,
    'type': '0x2'
}

signed_tx = web3.eth.account.signTransaction(tx, privatekey)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

