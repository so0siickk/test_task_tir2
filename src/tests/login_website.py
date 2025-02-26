from src.entities.classes import User, Wallet

test_email = "sawelysawin@yandex.ru"
password = "T7HCmpbt9MPB6nueakxsfL"
wallet1 = Wallet("test_key", "test address")
user1 = User(test_email, password, "twitter", wallet1)
wallet2 = Wallet("test_key1", "test address")
user2 = User("test@mail.ru", "password", "twitter", wallet2)
users = [user1,user2]
User.login_website(users)