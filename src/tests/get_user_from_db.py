import string
import secrets

from src.entities.classes import User, Wallet
from src.models.database import UserBase
from src.repositores.librarian import create_user, create_db_and_tables, get_by_email, get_by_id, get_by_twitter, \
    get_by_wallet


def create_password():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password


def create_email():
    alphabet = string.ascii_letters + string.digits
    while True:
        email = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in email)
                and any(c.isupper() for c in email)
                and sum(c.isdigit() for c in email) >= 3):
            break
    return email + "@gmail.com"


create_db_and_tables()
wallet = Wallet("test_key", "test_address")
user1 = User(create_email(), create_password(), "twitter", wallet)
first_note = UserBase(email=user1.get_email(), password=user1.get_password(), twitter=user1.get_twitter(),
                      wallet_address=user1.get_wallet().get_address(), wallet_key=user1.get_wallet().get_private_key())
create_user(first_note)

print(get_by_id(1))
print(get_by_email(user1.get_email()))
print(get_by_twitter(user1.get_twitter()))
print(get_by_wallet(wallet.get_address()))
