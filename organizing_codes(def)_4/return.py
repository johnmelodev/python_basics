# differences between using Function print and return

def display_exchange_rate(currency):
    if currency == 'usd':
        print(5.47)


display_exchange_rate('usd')


def get_exchange_rate(currency):
    if currency == 'usd':
        return 5.47


exchange_rate = get_exchange_rate('usd')
if exchange_rate > 5:
    print('Invest in American stocks')
else:
    print('Exchange rate not favorable')
