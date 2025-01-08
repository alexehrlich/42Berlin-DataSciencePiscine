import psycopg2 as pg
import subprocess 


def main():
    conn = pg.connect(  database = 'piscineds',
                        host = 'localhost',
                        user = 'aehrlich',
                        password = 'mysecretpassword',
                        port = '5432')

    cursor = conn.cursor()

    try:
        cursor.execute("""
                        CREATE TABLE items (
                            id BIGSERIAL NOT NULL PRIMARY KEY,
                            product_id BIGINT,
                            category_id BIGINT,
                            category_code TEXT,
                            brand VARCHAR(100) )
                        """)
        conn.commit()
        command = """
                    psql -U aehrlich -d piscineds -c "\\copy items(product_id, category_id, category_code, brand)
                    FROM '../subject/item/item.csv'
                    DELIMITER ',' CSV HEADER;"
                    """
        subprocess.run(command, shell=True)

    except pg.Error as err:
            print(err)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()