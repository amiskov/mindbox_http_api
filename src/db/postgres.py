import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()


class Database():
    conn = None

    def __init__(self):
        try:
            print("Connecting to PostgreSQL Database...")
            self.conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                port=os.getenv("POSTGRES_PORT"),
                cursor_factory=RealDictCursor,
            )
        except psycopg2.OperationalError as e:
            print(f"Could not connect to Database: {e}")
            sys.exit(1)

    def get_categories(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                c.name as category,
                array_remove(array_agg(DISTINCT p.name), NULL) as products
            FROM category as c
            left join category_product as cp on cp.category_id = c.id
            left join product as p on cp.product_id = p.id
            group by c.id
            order by c.name;
            '''
            cur.execute(q)
            return cur.fetchall()
        return []

    def get_products(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                p.name as product,
                array_remove(array_agg(DISTINCT c.name), NULL) as categories
            FROM product as p
            left join category_product as cp on cp.product_id = p.id
            left join category as c on cp.category_id = c.id
            group by p.id
            order by p.name;            
            '''
            cur.execute(q)
            return cur.fetchall()
        return []

    def get_prod_cat_pairs(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                p.name as product,
                c.name as category
            FROM product AS p
            FULL OUTER JOIN category_product AS cp ON cp.product_id = p.id
            FULL OUTER JOIN category AS c ON cp.category_id = c.id
            ORDER BY p.name;
            '''
            cur.execute(q)
            return cur.fetchall()
        return []

    def disconnect(self):
        if self.conn:
            print("Disconnecting database...")
            self.conn.close()
        else:
            print("Connection not found.")
