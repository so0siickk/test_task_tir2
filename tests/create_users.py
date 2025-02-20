from entities.classes import User
import string
import secrets

from repositores.librarian import insert_data_db, get_data_db


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


user1 = User(create_email(), create_password(),"twitter1","wallet1")
user2 = User(create_email(), create_password(), "twitter2", "wallet2")
insert_data_db(user1)
insert_data_db(user2)
print(get_data_db())

