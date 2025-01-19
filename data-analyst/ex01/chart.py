import psycopg2 as pg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def month(month_num: int) -> str:
    return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month_num - 1 % 12]

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
        cursor.execute("""
            SELECT 
                DATE(event_time) AS event_date, 
                COUNT(*) AS purchase_count,
                SUM(price) AS total_daily_sum
            FROM 
                customers
            WHERE 
                event_type = 'purchase' AND event_time < '2023-03-01'
            GROUP BY 
                event_date
            ORDER BY 
                event_date;
            """)
        
        purchase_records = cursor.fetchall()

        time_date = []
        purchase_count = []
        daily_sums = []
        monthly_sales = {}

        for record in purchase_records:
            time_date.append(record[0])
            purchase_count.append(record[1])
            daily_sums.append(record[2] / record[1])
            if month(record[0].month) in monthly_sales:
                monthly_sales[month(record[0].month)] += record[2]
            else:
                monthly_sales[month(record[0].month)] = record[2]

        fig, axes = plt.subplots(2, 2, figsize=(10, 10))

        axes[0][0].xaxis.set_major_locator(mdates.MonthLocator())  # Ticks at the start of each month
        axes[0][0].xaxis.set_major_formatter(mdates.DateFormatter('%b')) # Formatting to show short names
        axes[0][0].plot(time_date, purchase_count)
        axes[0][0].set_ylabel('Number of customers')
        axes[0][0].margins(x=0)
        axes[0][0].grid(color='gray')

        axes[0][1].bar(monthly_sales.keys(), monthly_sales.values(), color='lightblue')
        axes[0][1].set_ylabel('total sum in million')
        axes[0][1].set_axisbelow(True)
        axes[0][1].grid(True, axis='y')

        axes[1][0].xaxis.set_major_locator(mdates.MonthLocator())
        axes[1][0].xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        axes[1][0].stackplot(time_date, daily_sums, color='lightblue')
        axes[1][0].margins(x=0)
        axes[1][0].set_ylabel('average spend/customer')
        axes[1][0].set_axisbelow(True)
        axes[1][0].grid()

        axes[1][1].axis('off')


        plt.show()
            
    except pg.Error as err:
        print(err)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()