#  pip install web3

from web3 import Web3

url = "" ##put your rinkeby infura api key

abi_contract = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "initialMessage",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "message",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newMessage",
				"type": "string"
			}
		],
		"name": "setMessage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
account_a = "" ##put your public key here
key_a = "" ##put your private key here

contract_address = "0x9b59eAFE8630e39ab7D9c655F73cD136BdA98CD7"

web3 = Web3(Web3.HTTPProvider(url))

# Crear una funcion para desplegar el contrato

def read():
	address = web3.toChecksumAddress(contract_address)
	contract = web3.eth.contract(address=address, abi=abi_contract)
	data = contract.functions.message().call()
	print(data)

read()