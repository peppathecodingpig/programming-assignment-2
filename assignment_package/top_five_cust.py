def top_five_cust(df) -> list:
    #Need to review later for possible bugs
    counting_orders = df.groupby("CustomerID")["InvoiceNo"].nunique()

   
    counting_orders = counting_orders.sort_values(ascending=False)

   
    return counting_orders.iloc[:5].index.tolist()
    
