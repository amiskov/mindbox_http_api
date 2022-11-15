import sys
import logging
import psycopg
from psycopg.rows import dict_row
from core.config import config

log = logging.getLogger(__name__)

dsn = f'host={config.POSTGRES_HOST} ' + \
    f'dbname={config.POSTGRES_DB} ' + \
    f'user={config.POSTGRES_USER} ' + \
    f'password={config.POSTGRES_PASSWORD} ' + \
    f'port={config.POSTGRES_PORT}'


class Database():
    conn = None

    def __init__(self):
        try:
            log.info("Connecting to PostgreSQL Database...")
            self.conn = psycopg.connect(dsn, row_factory=dict_row)
        except psycopg.OperationalError as e:
            log.error(f"Could not connect to Database: {e}")
            sys.exit(1)

    def get_categories(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                c.name AS category,
                array_remove(array_agg(DISTINCT p.name), NULL) AS products
            FROM category AS c
            LEFT JOIN category_product AS cp ON cp.category_id = c.id
            LEFT JOIN product AS p ON cp.product_id = p.id
            GROUP BY c.id
            ORDER BY c.name;
            '''
            cur.execute(q)
            return cur.fetchall()
        return []

    def get_products(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                p.name AS product,
                array_remove(array_agg(DISTINCT c.name), NULL) AS categories
            FROM product AS p
            LEFT JOIN category_product AS cp ON cp.product_id = p.id
            LEFT JOIN category AS c ON cp.category_id = c.id
            GROUP BY p.id
            ORDER BY p.name;
            '''
            cur.execute(q)
            return cur.fetchall()
        return []

    def get_prod_cat_pairs(self):
        if self.conn:
            cur = self.conn.cursor()
            q = '''
            SELECT
                p.name AS product,
                c.name AS category
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
            log.info("Disconnecting database...")
            self.conn.close()
        else:
            log.error("Connection not found.")
