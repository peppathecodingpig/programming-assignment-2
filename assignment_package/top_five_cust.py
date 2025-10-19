def top_five_cust(df) -> list:
    # Count number of unique orders per customer
    counting_orders = df.groupby("CustomerID")["InvoiceNo"].nunique()

    # Sort descending (most orders first)
    counting_orders = counting_orders.sort_values(ascending=False)

    # Get first 5 CustomerIDs (index values)
    return counting_orders.iloc[:5].index.tolist()
    
