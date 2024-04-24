import argparse
import csv
from datetime import datetime
from solders.keypair import Keypair
from solders.pubkey import Pubkey
import base58


def create_wallets(number_of_wallets, filename):

    if filename:
        file = open(filename, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["Wallet Address", "Private Key"])

    for _ in range(number_of_wallets):
        # Create a new keypair
        keypair = Keypair()

        # Get the public key
        public_key = keypair.pubkey()

        # Convert keypair to base58
        private_key = base58.b58encode(bytes(keypair)).decode("utf-8")

        if filename:
            writer.writerow([public_key, private_key])
        else:
            print(f"PublicKey: {public_key} PrivateKey: {private_key}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Solana Wallets")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of wallets to generate")
    parser.add_argument("-o", "--output", default=None, help="Optional: Output file name")

    args = parser.parse_args()
    create_wallets(args.count, args.output)

    if args.output:
        print(f"Wallets saved to {args.output}")
