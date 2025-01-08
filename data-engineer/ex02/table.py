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
                        CREATE TABLE data_2022_oct (
                            id BIGSERIAL NOT NULL PRIMARY KEY,
                            event_time TIMESTAMP WITH TIME ZONE,
                            event_type VARCHAR(50),
                            product_id BIGINT,
                            price DECIMAL (20,2),
                            user_id BIGINT,
                            user_session UUID)
                        """)
        conn.commit()
        command = """
                    psql -U aehrlich -d piscineds -c "\\copy data_2022_oct(event_time, event_type, product_id, price, user_id, user_session)
                    FROM '../subject/customer/data_2022_oct.csv'
                    DELIMITER ',' CSV HEADER;"
                    """
        subprocess.run(command, shell=True)

    except pg.Error as err:
            print(err)
    

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()