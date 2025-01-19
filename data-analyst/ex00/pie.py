import psycopg2 as pg
import matplotlib.pyplot as plt

def main():
    try:
        conn = pg.connect(
            dbname='piscineds',
            user='aehrlich',
            password='mysecretpassword',
            host='localhost',
            port='5432'
        )

        cursor = conn.cursor()
    
    except pg.Error as err:
        print(err)

    try:
        values = []
        labels = []

        cursor.execute("""
            SELECT event_type, COUNT(*)
            FROM customers
            GROUP BY event_type;
        """)

        for record in cursor:
            labels.append(record[0])
            values.append(record[1])
        
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.show()

    except pg.Error as err:
        print(err)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()