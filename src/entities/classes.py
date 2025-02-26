import asyncio
import aiohttp
import time
from aptc import Account, new_client


class Wallet:
    def __init__(self, private_key, address):
        self.private_key = private_key
        self.address = address

    def get_private_key(self):
        return self.private_key

    def get_address(self):
        return self.address

    def set_private_key(self, private_key):
        self.private_key = private_key

    def set_address(self, address):
        self.address = address

    def make_daily_transaction(self):
        client = new_client()
        account = Account.load_key(self.private_key)
        account_address = account.address()
        payload = {
            'function': '0x3fa9e346261bdd3bdd7bbc57b1cb12b47a5ae8cb7531b6fa4759f524ffcac011::my_counter::increment',
            'type_arguments': [],
            'arguments': [
                self.address,
            ],
            'type': 'entry_function_payload'
        }
        txn_dict = {
            "sender": f"{account_address}",
            "sequence_number": str(client.get_account_sequence_number(account_address)),
            "max_gas_amount": str(8),
            "gas_unit_price": str(100),
            "expiration_timestamp_secs": str(int(time.time()) + 100),
            "payload": payload,
        }
        encoded = client.encode(txn_dict)
        signature = account.sign(encoded)
        txn_dict["signature"] = {
            "type": "ed25519_signature",
            "public_key": f"{account.public_key()}",
            "signature": f"{signature}",
        }
        tx = client.submit_transaction(txn_dict)

class User:
    def __init__(self, email: str, password: str, twitter: str, wallet: Wallet, balance=0, status="create"):
        self.email = email
        self.password = password
        self.twitter = twitter
        self.wallet = wallet
        self.balance = balance
        self.status = status

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_twitter(self):
        return self.twitter

    def get_wallet(self):
        return self.wallet

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_twitter(self, twitter):
        self.twitter = twitter

    def set_wallet(self, wallet: Wallet):
        self.wallet = wallet

    def set_balance(self, balance):
        self.balance = balance

    def set_status(self, status):
        self.status = status

    async def login_website(all_users: []):
        url = 'https://castile.world//api/guest/login HTTP/2'
        login_data = []
        for user in all_users:
            login_data.append({
                'email': user.get_email,
                'password': user.get_password,
                'login_button': '1'
            })
        async with aiohttp.ClientSession() as session:
            tasks = []
            for current_data in login_data:
                tasks.append(asyncio.create_task(session.post(url, data = current_data)))
                responses = await asyncio.gather(*tasks)

    async def registration_website(all_users:[]):
        url = 'https://castile.world//api/guest/register'
        registration_data = []
        for user in all_users:
            registration_data.append({
                'email': user.get_email,
                'code': "888888",
                'password': user.get_password,
                'password_confirm': user.get_password(),
                'agree': True
            })
        async with aiohttp.ClientSession() as session:
            tasks = []
            for current_data in registration_data:
                tasks.append(asyncio.create_task(session.post(url, data=current_data)))
                responses = await asyncio.gather(*tasks)