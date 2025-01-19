from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd

def main():
    engine = create_engine('postgresql+psycopg2://aehrlich:mysecretpassword@localhost:5432/piscineds')

    query = """
        SELECT price FROM customers
        WHERE event_type='purchase';
    """

    df_price = pd.read_sql(query, engine)

    query = """
        SELECT user_id, COUNT(*) AS cart_count,
        SUM(price)
        FROM customers
        WHERE event_type = 'cart'
        GROUP BY user_id
    """
    df_cart = pd.read_sql(query, engine)

    print(df_price.describe())

    fig, axes = plt.subplots(2, 2, figsize=(10,10))

    axes[0][0].boxplot(df_price['price'], orientation='horizontal')
    axes[0][0].grid()
    axes[0][0].set_xlabel('price')

    bplot = axes[0][1].boxplot(df_price['price'], orientation='horizontal', showfliers=False, patch_artist=True)
    axes[0][1].grid()
    axes[0][1].set_xlabel('price')
    bplot['boxes'][0].set_facecolor('red')

    axes[1][0].boxplot(df_cart['sum'], orientation='horizontal', showfliers=False, patch_artist=True)

    axes[1][1].axis('off')

    plt.show()


if __name__ == '__main__':
    main()