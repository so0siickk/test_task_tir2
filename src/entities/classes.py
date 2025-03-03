import asyncio
import aiohttp
import time
import requests
import tweepy.asynchronous
from aptc import Account, new_client
from random import shuffle


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


class Twitter:
    def __init__(self, nickname, bearer_token, api_key, api_secret, access_token, access_secret):
        self.nickname = nickname
        self.bearer_token = bearer_token
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_secret = access_secret

    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname

    async def make_retweet(self, tweet_id):
        client = tweepy.asynchronous.AsyncClient(self.bearer_token, self.api_key, self.api_secret, self.access_token,
                                                 self.access_secret)
        response_like = await client.like(tweet_id)
        response_retweet = await client.retweet(tweet_id)

    async def follow(self, user_id):
        client = tweepy.asynchronous.AsyncClient(self.bearer_token, self.api_key, self.api_secret, self.access_token,
                                                 self.access_secret)
        response = await client.follow_user(user_id)

    def get_tasks(self):
        all_tasks = []
        with requests.Session() as session:
            login_data = {
                'email': "email",
                'password': "password",
                'login_button': '1'
            }
            url = "https://castile.world//api/guest/login"
            response = session.post(url=url, data=login_data)
            response_json = response.json()
            bearer_token = response_json.get("data").get("auth")
            for number in range(11):
                try:
                    headers = {'Authorization': f'Bearer {bearer_token}'}
                    response = session.get(f"https://castile.world/gapi/task/v1/tasks?community_id={number}",
                                           headers=headers)
                    all_tasks += response.json().get("data").get("tasks")
                except Exception as e:
                    print(f"Заданий с id:{number} нет")
        retweet_numbers = []
        follow_numbers = []
        for index, task in enumerate(all_tasks):
            if "Repost" in task.get("description"):
                retweet_numbers.append(index)
            if ("Follow" in task.get("description")) and ("target=" in task.get("url")):
                follow_numbers.append(index)
        retweet_tasks = []
        follow_tasks = []
        for index in retweet_numbers:
            retweet_tasks.append({all_tasks[index].get("id"): all_tasks[index].get("url").split("target=")[1]})
        for index in follow_numbers:
            follow_tasks.append({all_tasks[index].get("id"): all_tasks[index].get("url").split("target=")[1]})
        shuffle(retweet_tasks)
        shuffle(follow_tasks)
        return retweet_tasks, follow_tasks

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
        url = 'https://castile.world/api/guest/login'
        login_data = []
        bearer_tokens = []
        for user in all_users:
            login_data.append({
                'email': user.get_email,
                'password': user.get_password,
                'login_button': '1'
            })
        async with aiohttp.ClientSession() as session:
            tasks = []
            for current_data in login_data:
                tasks.append(asyncio.create_task(session.post(url, data=current_data)))
            response = await asyncio.gather(*tasks)
            for current_response in response:
                bearer_tokens.append(current_response.get("data").get("auth"))

    async def registration_website(all_users: []):
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
            response = await asyncio.gather(*tasks)

    async def collect_rewards(all_users: [], all_tasks: []):
        url = 'https://castile.world/api/guest/login'
        url_tasks = "https://castile.world/gapi/task/v1/reward?id="
        login_data = []
        bearer_tokens = []
        for user in all_users:
            login_data.append({
                'email': user.get_email,
                'password': user.get_password,
                'login_button': '1'
            })
        async with aiohttp.ClientSession() as session:
            tasks = []
            for current_data in login_data:
                tasks.append(asyncio.create_task(session.post(url, data=current_data)))
            response = await asyncio.gather(*tasks)
            for current_response in response:
                bearer_tokens.append(current_response.get("data").get("auth"))
        async with aiohttp.ClientSession() as session:
            for current_token in bearer_tokens:
                headers = {'Authorization': f'Bearer {current_token}'}
                tasks = []
                for castile_task in all_tasks:
                    tasks.append(asyncio.create_task(session.post(url_tasks + str(castile_task), headers=headers)))
                response = await asyncio.gather(*tasks)
