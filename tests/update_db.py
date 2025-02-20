from entities.classes import User
import string
import secrets

from models.database import UserBase
from repositores.librarian import create_user, create_db_and_tables, get_by_id, update_status


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
user1 = UserBase(email = create_email(),password = create_password(),twitter = "twitter1",wallet = "wallet1", balance = 0)
user2 = UserBase(email = email2,password = create_password(),twitter = "twitter2",wallet = "wallet2", balance = 0)

create_user(user1)
create_user(user2)

update_status(1,"Ready")
update_status(email2, "Complete")

print(get_by_id(1))
print(get_by_id(2))