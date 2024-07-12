import pandas as pd

orders = pd.read_csv('dataset/orders.csv')
products = pd.read_csv('dataset/products.csv')
order_products_prior = pd.read_csv('dataset/order_products__prior.csv')

print(orders.head())
print(products.head())
print(order_products_prior.head())
