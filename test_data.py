import json
from database import Session
from models import Publishers, Book, Stock, Shop, Sale


def fill_test_data():
    with open("tests_data.json", "r") as file:
        test_data = json.load(file)
        print(test_data)

        model_to_test_data = {"publisher": Publishers,
                              "shop": Shop,
                              "book": Book,
                              "stock": Stock,
                              "sale": Sale}
        with Session() as s:
            for record in test_data:
                s.add(model_to_test_data.get(record.get("model"))(id=record.get("pk"), **record.get("fields")))
                s.commit()
