import asyncio

from src.entities.classes import User, Wallet

test_email = "email"
password = "password"
wallet1 = Wallet("test_key", "test address")
user1 = User(test_email, password, "twitter", wallet1)
wallet2 = Wallet("test_key1", "test address")
user2 = User("test@mail.ru", "password", "twitter", wallet2)
users = [user1, user2]
asyncio.run(User.login_website(users))