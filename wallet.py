import json
import base58

# Load the JSON file containing the wallet's private key
wallet_file = 'kopi.json'

try:
    with open(wallet_file, 'r') as file:
        wallet_data = json.load(file)

    # Assuming the private key is directly in the JSON object
    # Convert the private key to bytes and encode using base58
    encoded_private_key = base58.b58encode(bytes(wallet_data))

    # Print the encoded private key
    print("Encoded Private Key:", encoded_private_key)
except Exception as e:
    print(f"An error occurred: {e}")
