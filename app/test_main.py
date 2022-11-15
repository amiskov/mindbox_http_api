from typing import Optional
from fastapi.testclient import TestClient
from main import app
from repo import get_db
from models import Category, Product

p1 = Product(id="1", name="P1")
p2 = Product(id="2", name="P2")
p3 = Product(id="3", name="P3")

c1 = Category(id="1", name="C1")
c2 = Category(id="2", name="C2")

cats = [
    {
        'category': c1.name,
        'products': [p1.name, p2.name]
    },
    {
        'category': c2.name,
        'products': [p2.name, p3.name]
    },
]
prods = [
    {
        'product': p1.name,
        'categories': [c1.name]
    },
    {
        'product': p2.name,
        'categories': [c1.name, c2.name]
    },
    {
        'product': p3.name,
        'categories': [c2.name]
    },
]
pairs = [
    {
        'product': p1.name,
        'category': c1.name
    },
    {
        'product': p2.name,
        'category': c1.name
    },
    {
        'product': p2.name,
        'category': c2.name
    },
    {
        'product': p3.name,
        'category': c2.name
    },
]


class MockDb():
    def get_categories(self):
        return cats

    def get_products(self):
        return prods

    def get_prod_cat_pairs(self):
        return pairs


mock_db: Optional[MockDb] = None


def mock_get_db():
    global mock_db
    if mock_db is None:
        mock_db = MockDb()
    return mock_db


app.dependency_overrides[get_db] = mock_get_db

client = TestClient(app)


def test_categories():
    response = client.get("/api/v1/categories")
    assert response.status_code == 200
    assert response.json() == cats


def test_products():
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    assert response.json() == prods


def test_prod_cat_pairs():
    response = client.get("/api/v1/prod-cat-pairs")
    assert response.status_code == 200
    assert response.json() == pairs
