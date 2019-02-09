
# Define main function 
def main():
    """
    :return: 
    """
    # Rate
    usd_vs_rmb = 6.77

    # Input with unit
    currency_str_value = input("please input currency with unit:")

    # Get currency unit
    unit = currency_str_value[-3:]

    if unit == "CNY":
        exchange_rate = 1 / usd_vs_rmb

    elif unit == "USD":
        exchange_rate = usd_vs_rmb

    else:
        # Unexpected result
        exchange_rate = -1

    if exchange_rate != -1:
        input_money = eval(currency_str_value [:-3])
        # Define lambda function
        convert_currency = lambda x: x * exchange_rate
        # Call lambda function
        out_money = convert_currency(input_money)
        print("covert money", out_money)

    else:
        print("unsupported currency")

if __name__ == '__main__':
    main()
