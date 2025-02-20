from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from typing import Optional


class Base(DeclarativeBase):
    pass


class UserBase(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    twitter: Mapped[str] = mapped_column(String(30))
    wallet: Mapped[str] = mapped_column(String(30))
    balance: Mapped[Optional[int]] = mapped_column()
    status: Mapped[Optional[str]] = mapped_column(String(30), default= "Created")



    def __repr__(self) -> str:
            return (f"UserBase(id={self.id}, email={self.email}, password={self.password}, twitter={self.twitter},"
                    f" wallet={self.wallet}, balance={self.balance}, status={self.status})")