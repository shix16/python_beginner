
# Define function
def convert_currency(im,er):
    """
    :param im: input money
    :param er: exchange rate
    :return: output money
    """
    out = im * er
    return out

# Rate
usd_vs_rmb = 6.77

# Input with unit
currency_str_value = input("please input currency with unit:")

#while currency_str_value != "q":

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
    # Call defined function
    output_money = convert_currency(input_money,exchange_rate)
    print("covert money", output_money)

else:
    print("unsupported currency")

print("converter quit")
