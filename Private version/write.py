#  pip install web3

from web3 import Web3

url = "https://rinkeby.infura.io/v3/b17ec747232f4338b270ed85322ea834"

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

account_a = "0xE4783a07b97c7adC3320F393a1D386CB7A4180ec"
key_a = "e142ac12694913f478b39df66e10a7cf89dbab4a67ebd1efe94ba3f3b53c5bb3"

message = "Hello world from Pyhton"

contract_address = "0x9b59eAFE8630e39ab7D9c655F73cD136BdA98CD7"

web3 = Web3(Web3.HTTPProvider(url))

# Crear una funcion para desplegar el contrato

def write():
    address = web3.toChecksumAddress(contract_address)
    contract = web3.eth.contract(address=address, abi=abi_contract)
    nonce = web3.eth.getTransactionCount(account_a)

    parameter = {
        'nonce': nonce,
        'from': account_a,
        'gas': 500000,
        'gasPrice' : web3.toWei('21','gwei')
    }

    key = web3.eth.account.privateKeyToAccount(key_a)
    tx = contract.functions.setMessage(message).buildTransaction(parameter)
    signed = key.sign_transaction(tx)
    transaction = web3.eth.sendRawTransaction(signed.rawTransaction)
    print('https://rinkeby.etherscan.io/tx/' + transaction.hex())

write()