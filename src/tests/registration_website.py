from src.entities.classes import User, Wallet

test_email = "sawelysawin@yandex.ru"
password = "T7HCmpbt9MPB6nueakxsfL"
wallet = Wallet("test_key", "test address")
user1 = User(test_email, password, "twitter", wallet)
user1.registration_website()


