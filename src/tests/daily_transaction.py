from src.entities.classes import User, Wallet

test_email = "email"
password = "password"
wallet = Wallet("private_key",
                "address")
user1 = User(test_email, password, "twitter", wallet)
wallet.make_daily_transaction()