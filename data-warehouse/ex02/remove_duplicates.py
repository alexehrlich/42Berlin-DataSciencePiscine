import psycopg2 as pg

def main():
    conn = pg.connect(
        dbname = 'piscineds',
        user = 'aehrlich',
        password = 'mysecretpassword',
        host = 'localhost',
        port = '5432'
    )

    cursor = conn.cursor()

    print("Counting rows of table customers . . .")
    cursor.execute("""
        SELECT COUNT(*) FROM customers;
    """)
    print(f"Found {cursor.fetchone()[0]} rows in customer.\n")

    print("Counting duplicate rows in table customers. . .")
    cursor.execute("""
        SELECT SUM(cnt - 1) AS duplicate_cnt FROM (
            SELECT COUNT(*) AS cnt
            FROM customers
            GROUP BY event_type, product_id, price, user_id, user_session
            HAVING COUNT(*) > 1
        );
    """)
    print(f"Found {cursor.fetchone()[0]} duplicate rows in table customers.\n")

    print("Deleting duplicate rows from table customers . . .\n")
    cursor.execute("""
        CREATE TEMPORARY TABLE temp_customers AS
        SELECT DISTINCT ON (event_type, product_id, price, user_id, user_session) *
        FROM customers
        ORDER BY event_type, product_id, price, user_id, user_session;
    """)
    conn.commit()

    cursor.execute("""
        TRUNCATE customers;
    """)
    conn.commit()

    cursor.execute("""
        INSERT INTO customers
        SELECT * FROM temp_customers;
    """)

    cursor.execute("""
        DROP TABLE temp_customers;
    """)
    conn.commit()

    # print("Counting rows of table customers . . .")
    # cursor.execute("""
    #     SELECT COUNT(*) FROM customers;
    # """)
    # print(f"Customers has now {cursor.fetchone()[0]} rows.\n")


if __name__ == '__main__':
    main()