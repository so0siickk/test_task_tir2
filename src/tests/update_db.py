import string
import secrets

from src.entities.classes import User, Wallet
from src.models.database import UserBase
from src.repositores.librarian import create_user, create_db_and_tables, get_by_id, update_status, get_by_email


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
email2 = create_email()
wallet1 = Wallet("test_key", "test_key")
wallet2 = Wallet("test_key1", "test_key1")
user1 = User(create_email(), create_password(), "twitter1", wallet1)
user2 = User(email2, create_password(), "twitter1", wallet2)
first_note = UserBase(email=user1.get_email(), password=user1.get_password(), twitter=user1.get_twitter(),
                      wallet_address=user1.get_wallet().get_address(), wallet_key=user1.get_wallet().get_private_key())
second_note = UserBase(email=user2.get_email(), password=user2.get_password(), twitter=user2.get_twitter(),
                       wallet_address=user2.get_wallet().get_address(), wallet_key=user2.get_wallet().get_private_key())
create_user(first_note)
create_user(second_note)

update_status(1, "Ready")
update_status(email2, "Complete")

print(get_by_id(1))
print(get_by_email(email2))
