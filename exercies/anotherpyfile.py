def stock_info(company, country, price, curency):
    return f'company:{company}\nCountry{country}\nPrice:{price}\nCurrency:{curency}'

print(stock_info.__code__.co_varnames)    