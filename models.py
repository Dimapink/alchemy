import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from typing import Annotated

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Publishers(Base):
    __tablename__ = "publishers"

    id: Mapped[int_pk]
    name: Mapped[str]
    def __str__(self):
        return f"{self.id}: {self.name}"

class Shop(Base):
    __tablename__ = "shops"

    id: Mapped[int_pk]
    name: Mapped[str]


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int_pk]
    title: Mapped[str]
    id_publisher: Mapped[int] = mapped_column(ForeignKey("publishers.id", ondelete='CASCADE'))


class Stock(Base):
    __tablename__ = "stock"

    id: Mapped[int_pk]
    id_book: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete='CASCADE'))
    id_shop: Mapped[int] = mapped_column(ForeignKey("shops.id", ondelete='CASCADE'))
    count: Mapped[int]


class Sale(Base):
    __tablename__ = "sale"

    id: Mapped[int_pk]
    price: Mapped[float]
    date_sale: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    id_stock: Mapped[int] = mapped_column(ForeignKey("stock.id", ondelete='CASCADE'))
    count: Mapped[int]


