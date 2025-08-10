import pandas as pd
import numpy as np

def load_data():
    """
    Loads the datasets and specifies appropriate data types to optimize memory usage.
    Returns:
        tuple: A tuple containing the three pandas DataFrames: orders_df, order_products_df, products_df.
    """
    print("Loading data...")
    # Load orders data with optimized data types
    orders_df = pd.read_csv(
        "../data/orders.csv", 
        dtype={
            'order_id': np.int32,
            'user_id': np.int32,
            'eval_set': 'category',
            'order_number': np.int8,
            'order_dow': 'category',
            'order_hour_of_day': 'category',
            'days_since_prior_order': np.float32
        }
    )

    # Load order_products data with optimized data types
    order_products_df = pd.read_csv(
        '../data/order_products__prior.csv',
        dtype={
            'order_id': np.int32,
            'product_id': np.int32,
            'add_to_cart_order': np.int16,
            'reordered': 'category'
        }
    )

    # Load products data with optimized data types
    products_df = pd.read_csv(
        '../data/products.csv',
        dtype={
           'product_id': np.int32,
           'aisle_id': np.int16,
           'department_id': 'category'
        }
    )
    print("Data loaded successfully.")
    return orders_df, order_products_df, products_df


def sanitize_data(orders_df, order_products_df, products_df):
    """
    Performs data validation and sanitization checks.
    Args:
        orders_df (pd.DataFrame): The orders DataFrame.
        order_products_df (pd.DataFrame): The order_products DataFrame.
        products_df (pd.DataFrame): The products DataFrame.
    Returns:
        tuple: A tuple containing the three sanitized pandas DataFrames.
    """
    print("\nStarting data sanitization and validation...")

    # --- Data Consistency Checks ---
    # Check for primary key uniqueness in orders_df
    assert orders_df['order_id'].is_unique, "order_id in orders_df is not unique"
    
    # Check for referential integrity: ensure all order_id's in order_products_df exist in orders_df
    missing_orders = order_products_df.loc[~order_products_df['order_id'].isin(orders_df['order_id'])]
    if not missing_orders.empty:
        print(f"Warning: {len(missing_orders)} order items have an order_id not present in the orders table.")
    
    # Check for referential integrity: ensure all product_id's in order_products_df exist in products_df
    missing_products = order_products_df.loc[~order_products_df['product_id'].isin(products_df['product_id'])]
    if not missing_products.empty:
        print(f"Warning: {len(missing_products)} order items have a product_id not present in the products table.")

    # --- Null Value Checks ---
    print("\nChecking for null values:")
    print("Orders DataFrame:\n", orders_df.isnull().sum())
    print("\nOrder Products DataFrame:\n", order_products_df.isnull().sum())
    print("\nProducts DataFrame:\n", products_df.isnull().sum())
    
    # --- Outlier/Invalid Value Checks ---
    print("\nChecking for invalid values and outliers:")
    invalid_order_number = orders_df[orders_df['order_number'] <= 0]
    if not invalid_order_number.empty:
        print(f"Warning: {len(invalid_order_number)} orders have a non-positive order_number.")

    invalid_add_to_cart = order_products_df[order_products_df['add_to_cart_order'] <= 0]
    if not invalid_add_to_cart.empty:
        print(f"Warning: {len(invalid_add_to_cart)} order products have a non-positive add_to_cart_order.")

    # days_since_prior_order can be null for a user's first order, but not negative.
    invalid_days_since = orders_df[(orders_df['days_since_prior_order'] < 0) & (~orders_df['days_since_prior_order'].isnull())]
    if not invalid_days_since.empty:
        print(f"Warning: {len(invalid_days_since)} orders have a negative days_since_prior_order.")

    # Check for duplicated rows across all dataframes
    print("\nChecking for duplicated rows:")
    print(f"Orders duplicates: {orders_df.duplicated().sum()}")
    print(f"Order Products duplicates: {order_products_df.duplicated().sum()}")
    print(f"Products duplicates: {products_df.duplicated().sum()}")

    print("\nData sanitization complete.")
    return orders_df, order_products_df, products_df


def save_clean_data(orders_df, order_products_df, products_df):
    """
    Saves the cleaned DataFrames to new CSV files.
    Args:
        orders_df (pd.DataFrame): The cleaned orders DataFrame.
        order_products_df (pd.DataFrame): The cleaned order_products DataFrame.
        products_df (pd.DataFrame): The cleaned products DataFrame.
    """
    print("\nSaving cleaned data...")
    orders_df.to_csv("../data/clean_orders.csv", index=False)
    order_products_df.to_csv("../data/clean_order_products.csv", index=False)
    products_df.to_csv("../data/clean_products.csv", index=False)
    print("Cleaned data saved to new CSV files.")


if __name__ == "__main__":
    orders, order_products, products = load_data()
    orders, order_products, products = sanitize_data(orders, order_products, products)
    save_clean_data(orders, order_products, products)
