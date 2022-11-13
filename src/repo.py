from typing import Optional

from fastapi import Depends
from pydantic import BaseModel

from db.postgres import Database


class ProductWithCategories(BaseModel):
    name: str
    categories: list[str]


class CategoryWithProducts(BaseModel):
    name: str
    products: list[str]

class ProdCatPair(BaseModel):
    product: Optional[str]
    category: Optional[str]

db: Optional[Database] = None


def get_db():
    global db
    if db is None:
        db = Database()
    return db


class Repo:
    def __init__(self, db=Depends(get_db)):
        self.db = db

    def get_categories(self) -> list[CategoryWithProducts]:
        def to_category(r):
            return CategoryWithProducts(
                name=r['category'],
                products=r['products'],
            )
        return [to_category(r) for r in self.db.get_categories()]

    def get_products(self) -> list[ProductWithCategories]:
        def to_product(r):
            return ProductWithCategories(
                name=r['product'],
                categories=r['categories'],
            )
        return [to_product(r) for r in self.db.get_products()]

    def get_prod_cat_pairs(self) -> list[ProdCatPair]:
        def to_pair(r):
            return ProdCatPair(
                product=r['product'],
                category=r['category'],
            )
        return [to_pair(r) for r in self.db.get_prod_cat_pairs()]
