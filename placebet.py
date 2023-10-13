#pip install requests
#pip install solders
#pip install solana
from solana.transaction import Transaction
from solders.keypair import Keypair
from solana.rpc.api import Client
import requests
import json

id1 = 0
id2 = 1
side = "home" 
stake = 10
odds = 1.5
bettorAddr = "<your wallet address>"
url = f"https://api.purebet.io/bets/betBuilder?id1={id1}&id2={id2}&side={side}&stake={stake}&odds={odds}&bettorAddr={bettorAddr}"
#example URL
# url = "https://api.purebet.io/bets/betBuilder?id1=0&id2=1&side=home&stake=10&odds=1.5&bettorAddr=FnBD7DgBpVG1pEkhWhDayacPfN1qQuUrV2RGRocMb8aX"

response = requests.get(url)
response_text = response.text
data = json.loads(response_text)
raw_transaction = data["body"]

raw_transaction_bytes = bytes(tuple(raw_transaction))

transaction = Transaction.deserialize(raw_transaction_bytes)

# Initialize a client
client = Client("<RPC URL, Best to use a free one from quicknode rather than a public one>")

# Load your keypair
keypair = Keypair.from_base58_string("<your wallet private key, can also use other method such as from_bytes/from_seed if you have the keypair>")

# Sign the transaction
transaction.sign(keypair)

# Serialize the signed transaction
signed_transaction = transaction.serialize()

# Send the signed transaction
result = client.send_raw_transaction(signed_transaction)
print("Transaction result: ", result)