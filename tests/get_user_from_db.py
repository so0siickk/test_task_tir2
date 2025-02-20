from entities.classes import User
import string
import secrets

from models.database import UserBase
from repositores.librarian import create_user, create_db_and_tables, get_by_email, get_by_id, get_by_twitter, \
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

email1 = create_email()
twitter1 = "twitter1"
wallet1 = "wallet1"
user1 = UserBase(email = email1,password = create_password(),twitter = twitter1,wallet = wallet1, balance = 0)

create_user(user1)

print(get_by_id(1))
print(get_by_email(email1))
print(get_by_twitter(twitter1))
print(get_by_wallet(wallet1))
