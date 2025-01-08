import psycopg2 as pg
import subprocess 
import os

def table_exists(cursor, name: str) -> bool:
    cursor.execute("select exists(select * from information_schema.tables where table_name=%s)", (name,))
    return cursor.fetchone()[0]

def main():
    try:
        conn = pg.connect(  database = 'piscineds',
                            host = 'localhost',
                            user = 'aehrlich',
                            password = 'mysecretpassword',
                            port = '5432')

        cursor = conn.cursor()
    except pg.Error as err:
        print(err)
        exit(0)
    
    files = os.listdir('../subject/customer')
    table_names = [file.removesuffix('.csv') for file in files]

    for table_name in table_names:

        if table_exists(cursor, table_name):
            print(f"Table: {table_name} already exists.")
            continue

        try:
            cursor.execute(f"""
                            CREATE TABLE {table_name} (
                                id BIGSERIAL NOT NULL PRIMARY KEY,
                                event_time TIMESTAMP WITH TIME ZONE,
                                event_type VARCHAR(50),
                                product_id BIGINT,
                                price DECIMAL (20,2),
                                user_id BIGINT,
                                user_session UUID)
                            """)
            conn.commit()
            print(f"Created table: {table_name}")
            print(f"Copying to table: {table_name} ...")
            command = f"""
                        psql -U aehrlich -d piscineds -c "\\copy {table_name}(event_time, event_type, product_id, price, user_id, user_session)
                        FROM '../subject/customer/{table_name}.csv'
                        DELIMITER ',' CSV HEADER;"
                        """
            subprocess.run(command, shell=True)

        except pg.Error as err:
                print(err)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()