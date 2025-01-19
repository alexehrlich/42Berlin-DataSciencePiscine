import psycopg2 as pg

def main():
    conn = pg.connect(
        dbname='piscineds',
        user='aehrlich',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )

    cursor = conn.cursor()

    print("Creating merged table between customers and items")
    cursor.execute("""
        CREATE TABLE customers_items AS
        SELECT c.*, i.category_id, i.category_code, i.brand
        FROM customers c
        LEFT JOIN items i
        ON c.product_id = i.product_id
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
