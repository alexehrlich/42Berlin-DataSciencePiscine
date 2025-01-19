from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    engine = create_engine('postgresql+psycopg2://aehrlich:mysecretpassword@localhost:5432/piscineds')

    query = """
        SELECT COUNT(*) as interactions,
        SUM(price) as total_spend,
        COUNT(*) FILTER (WHERE event_type='view') as view_count,
        COUNT(*) FILTER (WHERE event_type = 'cart') as cart_count,
        COUNT(*) FILTER (WHERE event_type='purchase') as purchase_count,
        COUNT(*) FILTER (WHERE event_type='remove_from_cart') as remove_count
        FROM customers
        GROUP BY user_id;
        """

    df = pd.read_sql(query, engine)

    print(df.describe())

    print(df.head())
    
    sns.pairplot(df)
    plt.show()

if __name__ == '__main__':
    main()