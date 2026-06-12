def stock_tracker():

    stocks = {
        "TCS": 3500,
        "INFY": 1500,
        "WIPRO": 250,
        "HCL": 1200,
        "MICRO":180,
    }

    total = 0

    print("Stock Portfolio Tracker")

    while True:
        stock = input("Enter stock name (or type done): ").upper()

        if stock == "DONE":
            break

        if stock in stocks:
            quantity = int(input("Enter quantity: "))

            value = stocks[stock] * quantity
            total = total + value

            print("Stock Value =", value)

        else:
            print("Stock not found")

    print("Total Portfolio Value =", total)


stock_tracker()