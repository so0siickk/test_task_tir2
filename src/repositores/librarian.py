from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from src.models.database import UserBase

current_file = Path(__file__)
parent_dir = current_file.parent
db_path = parent_dir.parent / 'models' / 'database.db'
DB_URL = f'sqlite:///{db_path}'
engine = create_engine(DB_URL, echo=True)


def create_db_and_tables() -> None:
    UserBase.metadata.create_all(engine)


def create_user(user: UserBase) -> None:
    session = sessionmaker(engine)
    with session() as session:
        try:
            session.add(user)
        except:
            session.rollback()
            raise
        else:
            session.commit()


def get_by_id(id: int, session=None) -> UserBase:
    if session is not None:
        statement = select(UserBase).where(UserBase.id == id)
        db_object = session.scalars(statement).one()
        return db_object
    session = sessionmaker(engine)
    with session() as session:
        statement = select(UserBase).where(UserBase.id == id)
        db_object = session.scalars(statement).one()
        return db_object


def get_by_email(email: str, session=None) -> UserBase:
    if session is not None:
        statement = select(UserBase).where(UserBase.email == email)
        db_object = session.scalars(statement).one()
        return db_object
    session = sessionmaker(engine)
    with session() as session:
        statement = select(UserBase).where(UserBase.email == email)
        db_object = session.scalars(statement).one()
        return db_object


def get_by_twitter(twitter: str, session=None) -> UserBase:
    if session is not None:
        statement = select(UserBase).where(UserBase.twitter == twitter)
        db_object = session.scalars(statement).one()
        return db_object
    session = sessionmaker(engine)
    with session() as session:
        statement = select(UserBase).where(UserBase.twitter == twitter)
        db_object = session.scalars(statement).one()
        return db_object


def get_by_wallet(wallet_address: str, session=None) -> UserBase:
    if session is not None:
        statement = select(UserBase).where(UserBase.wallet_address == wallet_address)
        db_object = session.scalars(statement).one()
        return db_object
    session = sessionmaker(engine)
    with session() as session:
        statement = select(UserBase).where(UserBase.wallet_address == wallet_address)
        db_object = session.scalars(statement).one()
        return db_object


def update_status(identifier: int | str, new_status: str) -> None:
    session = sessionmaker(engine)
    with session() as session:
        try:
            if isinstance(identifier, int):
                updated_user = get_by_id(identifier, session=session)
            if isinstance(identifier, str):
                updated_user = get_by_email(identifier, session=session)
            updated_user.status = new_status
            session.merge(updated_user)
        except:
            session.rollback()
            raise
        else:
            session.commit()
