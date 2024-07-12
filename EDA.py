import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    orders = pd.read_csv('dataset/instacart-market-basket-analysis/orders.csv')
    products = pd.read_csv('dataset/instacart-market-basket-analysis/products.csv')
    order_products_prior = pd.read_csv('dataset/instacart-market-basket-analysis/order_products__prior.csv')
    return orders, products, order_products_prior


def analyze_data(orders, products, order_products_prior):
    print("Orders DataFrame Head:")
    print(orders.head())
    print("\nProducts DataFrame Head:")
    print(products.head())
    print("\nOrder Products Prior DataFrame Head:")
    print(order_products_prior.head())


def visualize_data(orders):
    orders['order_hour_of_day'].hist()
    plt.title('Distribution of Orders by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Orders')
    plt.show()


if __name__ == "__main__":
    data_orders, data_products, data_order_products_prior = load_data()
    analyze_data(data_orders, data_products, data_order_products_prior)
    visualize_data(data_orders)
