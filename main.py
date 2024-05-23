from database import Database
from test_data import fill_test_data
from queries import Queries


def printer(payload):
    print("-"*20)
    if not payload:
        print("Ничего не нашлось")
    else:
        for row in payload:
            title = row[0]
            shop = row[1]
            price = row[2]
            purchase_date = row[3].strftime("%d-%m-%Y")
            print(f"{title} | {shop} | {price} | {purchase_date}")


if __name__ == "__main__":
    Database.create_tables()
    fill_test_data()
    print("Поиск по id")
    x = Queries.select_publisher(1)
    printer(x)
    print("Поиск по автору")
    y = Queries.select_publisher("O’Reilly")
    printer(y)
