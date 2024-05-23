from models import Publishers, Book, Shop, Sale, Stock
from database import Session
from sqlalchemy import select


class Queries:

    @staticmethod
    def select_publisher(publisher: str | int):
        with (Session() as s):
            q = select(Book.title, Shop.name, Sale.price, Sale.date_sale
                       ).join(Book, Publishers.id == Book.id_publisher
                              ).join(Stock, Stock.id_book == Book.id
                                     ).join(Shop, Shop.id == Stock.id_shop
                                            ).join(Sale, Sale.id_stock == Stock.id).select_from(Publishers)
            if isinstance(publisher, int):
                q = q.filter(Publishers.id == publisher)
            else:
                q = q.filter(Publishers.name.like(publisher))
            result = s.execute(q)
            return result.all()
