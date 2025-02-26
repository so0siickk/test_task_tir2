from src.entities.classes import User, Wallet

test_email = "sawelysawin@yandex.ru"
password = "T7HCmpbt9MPB6nueakxsfL"
wallet = Wallet("0xb35fd87c2af4ccfce62919185cc6945fa194dbfd43f644bc9cb292ed8049eca9",
                "0x3c65bad80a6bcaec1af2f97e3e0dd70447fd06f522805d98be50a90c0c295ade")
user1 = User(test_email, password, "twitter", wallet)
wallet.make_daily_transaction()
