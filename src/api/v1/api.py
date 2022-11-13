from fastapi import APIRouter, Depends
from models import Category, Product
from repo import CategoryWithProducts, ProdCatPair, ProductWithCategories, Repo


router = APIRouter()


@router.get('/categories', response_model=list[CategoryWithProducts], tags=["categories"])
async def categories(repo: Repo = Depends()) -> list[CategoryWithProducts]:
    return repo.get_categories()


@router.get('/products', response_model=list[ProductWithCategories], tags=["products"])
async def products(repo: Repo = Depends()) -> list[ProductWithCategories]:
    return repo.get_products()

@router.get('/prod-cat-pairs', response_model=list[ProdCatPair], tags=["products"])
async def prod_cat_pairs(repo: Repo = Depends()) -> list[ProdCatPair]:
    return repo.get_prod_cat_pairs()
