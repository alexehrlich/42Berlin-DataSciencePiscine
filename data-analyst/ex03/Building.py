from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd

def main():
    engine = create_engine('postgresql+psycopg2://aehrlich:mysecretpassword@localhost:5432/piscineds')

    query = """
        SELECT user_id, COUNT(*), SUM(price)
        FROM customers
        WHERE event_type='purchase'
        GROUP BY user_id;
    """

    df = pd.read_sql(query, engine)

    fig, axes = plt.subplots(1, 2, figsize=(10, 6))

    axes[0].hist(df['count'], bins=[0, 10, 20, 30, 40])
    axes[0].set_ylabel('customers')
    axes[0].set_xlabel('frequency')

    axes[1].hist(df['sum'], bins=[0, 50, 100, 150, 200, 250, 300, 350])
    axes[1].set_ylabel('customers')
    axes[1].set_xlabel('monetary value')

    plt.show()

if __name__ == '__main__':
    main()